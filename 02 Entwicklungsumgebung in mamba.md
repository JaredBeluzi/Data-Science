# Idee
Wenn man lokal entwickelt, benutzt man in der Regel die aktuelle Version von Software wie Python und der einzelnen Packages.
Dies kann dazu führen, dass nach einem Update von einzelnen Packages alter Code nicht mehr funktioniert, weil bestimmte Befehle nicht geändert wurden oder es zu Konflikten zwischen einzelnen Packages kommt.
Aus diesem Grund kann es sinnvoll sein eine Entwicklungsumgebung für jedes Code-Projekt zu definieren, in dem die Software-Version für alle Packages stabil bleibt.
Das kann durch die Wahl von mamba als Package-Manager erreicht werden
# mamba
Es gibt 3 typische Package-Manager. Diese sind:
- pip (Standard, installiert Packages lokal, kann Konflikte zwischen Modulsversionen hervorrufen)
- conda (kann virtuelle Umgebungen erstellen die Konflikte zwischen Modulen verhindert, kostet Geld)
- mamba (ähnliche zu conda, aber kostenlos)
# Anwendung
Wenn man Packages installiert, dann nur innerhalb einer virtuellen Umgebung. Startet man ein Projekt, tut man dies dann innerhalb einer festen virtuellen Umgebung, in der die Software-Versionen gleich bleiben.
https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html

## create, edit, delete environment
- `mamba env list`                 show list of environments 
- `mamba create -n env_name`       create environment
- `mamba activate env_name`        activate environment
- `mamba deactivate`               deactivate environment 
- `mamba install -n env_name jupyterlab -c conda-forge`  install a python package inside an environment from the outside
- `mamba update -n env_name --all` update all packages inside an environment
- `mamba env remove -n env_name`   delete environment

## working inside an enviroment (after activating an env this only affects the env itself) 
- `mamba install jupyterlab -c conda-forge` you can install packages 
- `jupyter lab`                             you can start jupyter lab like this

## best packages to install
- `mamba list`              shows list of packages installed
- `mamba install jupyterlab -c conda-forge` in jupyter lab some other packages are automatically included, like pandas and numpy
- `mamba install matplotlib` basic data visualisation
- `mamba install seaborn`    for visualization of data beyond matplotlib
- `mamba install scikit-learn`    contains statistical models
- `mamba install pyodbc`     for connections with MS SQL Server
- `mamba install sqlalchemy` needs pyodbc. for importing data from MS SQL Server and executing sql code in python
