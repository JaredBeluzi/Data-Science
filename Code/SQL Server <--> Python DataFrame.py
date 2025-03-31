# MS SQL Server <-> DataFrame

import pandas as pd
import pyodbc
import sqlalchemy as sa
#import os

DRIVER = "ODBC Driver 18 for SQL Server"
HOST = "XX.XX.XXX.XXX" # use SELECT CONNECTIONPROPERTY('local_net_address') to get the IP
DATABASE = "Ergebnisse"
USER = "user_name"
PASSWORD = "password"  # you can use os.environ['user_pwd'] to put this part into a local file

engine_url = sa.engine.URL.create(
        "mssql+pyodbc",
        host=HOST,
        username=USER,
        password=PASSWORD,
        database=DATABASE,
        query=dict(driver=DRIVER, TrustServerCertificate='yes') # add Trusted_connection='yes' when working on a Windows machine
    )
engine = sa.create_engine(engine_url, future=True, fast_executemany=True)

# importing data
df = pd.read_sql(f"SELECT * FROM S_12345", engine)

# exporting data
df.to_sql('DS_Inflation', con=engine, if_exists='replace', index=False)
