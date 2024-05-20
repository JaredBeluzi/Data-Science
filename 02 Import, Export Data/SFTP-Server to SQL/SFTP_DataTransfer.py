'''File Transfer and Import for Davaso Data from SFTP-Server'''

import argparse
from datetime import datetime
from loguru import logger
import os
import platform
import zipfile

import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from helpers.envandlogs import ConfigLoadersandLogging as EnvnLog
import helpers.pandas2sql as pdsqlalch
import helpers.netdrive_mount as netdrvmnt
from connections.connection_sftp import SftpHandler


class DataTransfer:

    def __init__(self, targetdirs_vars: {str}):
        self.rmt_files = []
        self.file_ext = targetdirs_vars['file_extensions']
        self.path_local = targetdirs_vars['download_dirpath']

        if not self.file_ext:
            # download all files
            self.lcl_exstfiles = [filename for folder, dirs, files in os.walk(self.path_local) if
                                  folder == self.path_local for filename in files]
        else:
            self.lcl_exstfiles = [filename for folder, dirs, files in os.walk(self.path_local) if
                                  folder == self.path_local for filename in files if
                                  filename.endswith(tuple(self.file_ext))]

    @logger.catch
    def download_files(self, logindata: [str], sftp_vars: {str}) -> [str]:

        remote_uri = sftp_vars['remote_uri']
        remote_archive_uri = sftp_vars['remote_archive_uri']
        succ_files = []

        with SftpHandler.connect(**logindata) as ssh_conn:
            with ssh_conn.open_sftp() as sftp_sess:
                files, _, _ = SftpHandler.get_dirlist(sftp_sess, remote_uri)

                self.rmt_files = [file for file in files if file.endswith(tuple(self.file_ext))]

                if not self.rmt_files:
                    logger.warning("No files available for download on server!")

                else:

                    for file in self.rmt_files:

                        if file in self.lcl_exstfiles:
                            continue

                        else:
                            path_remote_curr = remote_uri + '/' + file
                            filepath_local = os.path.join(self.path_local, file)
                            remote_filestat = sftp_sess.stat(path_remote_curr)

                            try:
                                # Download file and move to remote archive, if given
                                SftpHandler.download(sftp_sess, path_remote_curr, filepath_local)

                                # reset times of local file to server times
                                os.utime(filepath_local, (remote_filestat.st_atime, remote_filestat.st_mtime))

                                # add to succ_list
                                logger.info(f'Successfully downloaded "{file}"')
                                succ_files.append(file)

                                if remote_archive_uri != '':
                                    pass
                                    remote_path_new = remote_archive_uri + '/' + file
                                    SftpHandler.move_remotepath(sftp_sess, path_remote_curr, remote_path_new)

                            except Exception as err:
                                logger.exception(f"Error downloading: {path_remote_curr}. More details given:\n", err)

        return succ_files

    @logger.catch
    def unzipper(self, file_list: [str], lclpath_unzip: os.PathLike | str) -> [str]:

        succ_list = []

        for file in file_list:
            path_file_curr = os.path.join(self.path_local, file)
            zipfile_stat = os.stat(path_file_curr)

            try:
                with zipfile.ZipFile(path_file_curr, 'r') as zip_f:
                    for zip_entry in zip_f.infolist():
                        zip_f.extract(zip_entry, lclpath_unzip)
                        entry_filepath = os.path.join(lclpath_unzip, zip_entry.filename)
                        os.utime(entry_filepath, (zipfile_stat.st_atime, zipfile_stat.st_mtime))
                        succ_list.append(entry_filepath)

                logger.info(f'Successfully extracted "{file}"')

            except Exception as err:
                logger.exception(f"Error unzipping: {path_file_curr}. More details given:\n", err)

        return succ_list

    @logger.catch
    def file2sql_import(self, file_list: [str], import_info: [str], env_path: os.PathLike | str) -> [str]:

        succ_list = []
        for file2import in import_info:
            # import info holds all relevant variables to import specific files,
            # i.e. filetype, pandas_readin_vars and the respective sql server and tables

            # 0) Get variables
            filename_ident = file2import['filename_ident']
            file_ext = file2import['file_ext']
            file_csvinfo = file2import['csv_readinfo']
            file_writeinfo = file2import['sql_writeinfo']

            # 1) load server credentials and add to sql_info-dict
            sql_serverinfo = file2import['sql_serverinfo']
            servername = sql_serverinfo.pop('servername')  # pop this key to be able to use the dict later

            # 2) load env info for sql server
            sqlserver_env = os.path.join(env_path, servername + '.env')
            sqlserver_crdtls = EnvnLog.load_server_crdtls(sql_serverinfo['sql_type'], servername, sqlserver_env)
            sql_serverinfo.update(sqlserver_crdtls)

            for filepath in file_list:

                if filename_ident in filepath:
                    # the identification search string is found in filepath
                    # --> It is to be imported
                    if file_ext in ['.csv', '.txt'] and filepath.endswith(tuple(file_ext)):
                        # The relevant file is a txt or csv file --> use csv import
                        # load sqlalchemy engine
                        engine = pdsqlalch.get_sqlalchemy_engine(**sql_serverinfo)

                        if engine is not None:
                            # 1) read csv data in chunks to pandas and write to sql datatable
                            # returns success of total process
                            filename = os.path.basename(filepath)
                            current_time = datetime.now()
                            # define columns to add to data. The key equals the col name,
                            # value tuple defines the column position (start at 0) and column values
                            add_cols = {'Dateiname': (0,filename),
                                        'Importdatum': (1, current_time)}

                            succ_csv2db = pdsqlalch.csv2db(filepath, engine, file_csvinfo, file_writeinfo, add_cols)
                        else:
                            logger.error('Error establishing a SQL server connection.')
                            break

                        # 2) move files to subfolders depending on result of import
                        basepath = os.path.split(filepath)[0]
                        file = os.path.split(filepath)[1]
                        if succ_csv2db:
                            succ_list.append(filepath)
                            new_filepath = os.path.join(basepath, 'fehlerfrei', file)
                            logger.info(f'Successfully imported "{file}" to SQL database.')
                        else:
                            new_filepath = os.path.join(basepath, 'fehlerhaft', file)
                            logger.error(f'Error importing "{file}" to SQL database.')

                        if not os.path.exists(os.path.dirname(new_filepath)):
                            # Create subfolder if not existent
                            os.makedirs(os.path.dirname(new_filepath))

                        os.rename(filepath, new_filepath)

                else:
                    continue
        return succ_list


@logger.catch
def load_targetdir_vars(config_dict: {}) -> {}:

    # check if a network share is used
    targetdirs_vars = config_dict['targetdirs_vars']

    if targetdirs_vars['netdrive']:

        # load paths for netdrive
        mount_info = targetdirs_vars['netdrive_mount']
        netdrive_path = mount_info['path']
        mount_path = mount_info['mountpath']
        netdrive_type = mount_info['type']
        netdrive_name = mount_info['name']

        #  1.1) load network drive credentials
        servers_crdtlspath = config_dict['servers_crdtlspath']
        netdrive_envfile = os.path.join(servers_crdtlspath, netdrive_name + '.env')
        netdrive_crdtls = EnvnLog.load_server_crdtls('netdrive',
                                                     netdrive_name,
                                                     netdrive_envfile)

        # 1.2) Mount netdrive
        netdrive_mntd = netdrvmnt.mount_netdrive(netdrive_type, netdrive_path, mount_path, **netdrive_crdtls)
        if not netdrive_mntd:
            logger.error('Mounting netdrive failed. See logs!')

        if platform.system() == 'Windows':
            path_delimiter = '\\'
        else:
            path_delimiter = '/'
        # 2) transform network share paths to unix format
        targetdirs_vars_tmp = targetdirs_vars.copy()
        for k, v in targetdirs_vars_tmp.items():
            if k.endswith('dirpath'):
                netdir_path = targetdirs_vars_tmp[k]
                if netdrive_type == 'windows':
                    netdir_path = path_delimiter.join(netdir_path.split('\\'))
                else:
                    netdir_path = path_delimiter.join(netdir_path.split('/'))
                targetdirs_vars[k] = os.path.join(mount_path, netdir_path)
            else:
                pass

        del targetdirs_vars_tmp

    return targetdirs_vars


if __name__ == "__main__":

    # 0) Construct argparser to collect user arguments
    arg_parser = argparse.ArgumentParser(description="SFTP-DataTransfer",
                                         formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    arg_parser.add_argument("-cfg", "--config-filepath", action='store',
                            help="Local path to configuration yaml-file", required=True)

    arg_parser.add_argument("--csvimport-only", action='store_true',
                            help="Import already downloaded csv file according to yaml-file")


    # 1) Collect user arguments and retrieve filepath
    args = vars(arg_parser.parse_args())
    yaml_file = args['config_filepath']
    local_csvimport = args['csvimport_only']

    path_filedir = os.path.dirname(os.path.abspath('__file__'))
    yml_filepath = os.path.join(yaml_file)

    # 2) load config data and start logging
    cfgs_loggers = EnvnLog(yml_filepath)
    cfgs_loggers.instantiate_loggers()

    # 3) Load target directory pathes and mount netdrive if applicable
    targetdirs_vars = load_targetdir_vars(cfgs_loggers.cfgs)
    # local machine vars and network drive paths

    # set network logfile drive, if opted for. Explicitly add at last to be able to unregister it easily
    netdrive_dirpath = targetdirs_vars.get('netdrive_logfile_dirpath')
    if netdrive_dirpath is not None:
        netdrive_logfile = netdrive_dirpath + cfgs_loggers.cfgs['transfer_name'] + '.log'
        # add logger to loggers_idlist
        cfgs_loggers.logger_ids['netdrive_log'] = cfgs_loggers.add_loggersink(netdrive_logfile)

    # Get file transfer name
    transfer_name = cfgs_loggers.cfgs['transfer_name']
    servers_crdtlspath = cfgs_loggers.cfgs['servers_crdtlspath']

    # 4) SFTP server settings
    sftpserver_vars = cfgs_loggers.cfgs['sftpservervars']
    sftp_servername = sftpserver_vars['servername']
    sftp_envfile = os.path.join(servers_crdtlspath, sftp_servername + '.env')
    sftp_hostkey = os.path.join(servers_crdtlspath, sftpserver_vars['server_hostkey'])

    sftp_logindata = EnvnLog.load_server_crdtls('sftp', sftp_servername, sftp_envfile)
    sftp_logindata['hostkey'] = sftp_hostkey

    # 5) DB Import vars
    sql_import_vars = cfgs_loggers.cfgs['import2sql']

    # 6) Start Data Transfer
    data_trans = DataTransfer(targetdirs_vars)
    imported_files = []
    downld_files = []
    exctrd_files = []

    if local_csvimport:

        # 7) Manual SQL Import for debugging and special files
        unzip_folder = targetdirs_vars['local_unzip_dirpath']
        import_filepathlist = [os.path.join(unzip_folder, filename) for folder, dirs, files in os.walk(unzip_folder)
                               if folder == unzip_folder for filename in files]

        print('Manual file(s) import:', import_filepathlist)
        logger.info('Manual file Import')

        imported_files = data_trans.file2sql_import(import_filepathlist,
                                                    sql_import_vars['import_info'], servers_crdtlspath)
    else:
        # 8) Download Files
        downld_files = data_trans.download_files(sftp_logindata, sftpserver_vars)

        # # 9) Optional Unzip Files
        if '.zip' in targetdirs_vars['file_extensions']:
            zip_files = [file for file in downld_files if file.endswith(('.zip'))]
            exctrd_files = data_trans.unzipper(zip_files, targetdirs_vars['local_unzip_dirpath'])
        else:
            exctrd_files = []

        # 10) Optional Import files to SQL Database
        if sql_import_vars['import_data']:

            if not exctrd_files:
                import_filepathlist = [os.path.join(data_trans.path_local, file) for file in downld_files]
            else:
                import_filepathlist = exctrd_files

            imported_files = data_trans.file2sql_import(import_filepathlist,
                                                        sql_import_vars['import_info'], servers_crdtlspath)

    # 11) Finish Data transfer and write result to log
    logger.info(
        f"File transfer '{transfer_name}' finished! {len(downld_files)} file(s) downloaded, "
        f"{len(exctrd_files)} successfully extracted. {len(imported_files)} files(s) imported to DB")

    # 12) Unmount network drive if used
    if targetdirs_vars['netdrive']:
        if targetdirs_vars.get('netdrive_logfile_dirpath') is not None:
            # 11.1) De-register network drive logfile logger, if used
            logger.remove(cfgs_loggers.logger_ids['netdrive_log'])
        # 11.2) Unmount network drive
        netdrive_unmounted = netdrvmnt.unmount_netdrive(targetdirs_vars['netdrive_mount']['type'],
                                                      targetdirs_vars['netdrive_mount']['mountpath'])
        if not netdrive_unmounted:
            logger.error('Unmounting netdrive failed. See logs!')
