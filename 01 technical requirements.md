# 1. Hardware
It is recommended to work on a strong remote server. You can rent out space on a cloud server.
Example requirements:
- CPU: 10 cores
- RAM: 64GB
- SSD: 250 GB

# 2. OS
A linux version is recommended, because it makes installing and changing necessary programs and packages easier. Linux is better designed for programmers in my opinion.
Windows has the advantage of a better integration of Visual Studio Code, which is in my opinion the best IDE at the moment.

# 3. Software
## python
You need to install the latest python version.
https://www.python.org/downloads/

## mamba
There are 3 common python package managers. These are
- pip (standard, install packages locally, can create version conflicts between modules)
- conda (can create virtual environments, prevents version conflicts between modules, costs money)
- mamba (similar to conda but free)
Mamba is the best package manager and should be installed on your machine. 
When you install packages only do this inside a virtual environment (see mamba.md in this folder).
https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html

## Firefox
When using the python module Jupyter Lab, you need a browser, in which the module can start.
I highly recommend Firefox for this.

## VS Code + Copilot
Coding is much more efficient with an AI Tool like Copilot.
For that reason install VS Code as an IDE and use Github Copilot.

## ChatGPT
When it comes to structural questions or brainstorming for ideas, ChatGPT is very good.
It is also a good partner with Copilot to find the solution for coding problems.

# 4. mamba

create, edit, delete environment
- `mamba env list`                 show list of environments 
- `mamba create -n env_name`       create environment
- `mamba activate env_name`        activate environment
- `mamba deactivate`               deactivate environment 
- `mamba install -n env_name jupyterlab -c conda-forge`  install a python package inside an environment from the outside
- `mamba update -n env_name --all` update all packages inside an environment
- `mamba env remove -n env_name`   delete environment

working inside an enviroment (after activating an env this only affects the env itself) 
- `mamba install jupyterlab -c conda-forge` you can install packages 
- `jupyter lab`                             you can start jupyter lab like this

best packages to install
- `mamba list`              shows list of packages installed
- `mamba install jupyterlab -c conda-forge` in jupyter lab some other packages are automatically included, like pandas and numpy
- `mamba install matplotlib` basic data visualisation
- `mamba install seaborn`    for visualization of data beyond matplotlib
- `mamba install sklearn`    contains statistical models
- `mamba install pyodbc`     for connections with MS SQL Server
- `mamba install sqlalchemy` needs pyodbc. for importing data from MS SQL Server and executing sql code in python
