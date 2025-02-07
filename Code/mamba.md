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

## Entwicklungsumgebung erstellen, ändern und löschen
```
mamba env list                  # Liste der environments 
mamba create -n env_name        # erstelle environment
mamba activate env_name         # aktiviere environment
mamba deactivate                # deaktiviere environment 
mamba install -n env_name jupyterlab -c conda-forge    # installiere python package in environment außerhalb des environments
mamba update -n env_name        # update alle packages in environment
mamba env remove -n env_name    # lösche environment
```

## in Entwicklungsumgebung arbeiten (beinfluss nur das aktivierte env) 
```
mamba install jupyterlab -c conda-forge`  # installiere package innerhalb environment
jupyter lab                               # starte jupyter lab in environment
```

## best packages to install
```
mamba list                               # Liste installierter packages
mamba install jupyterlab -c conda-forge  # beinhaltet pandas und numpy
mamba install matplotlib                 # basic Visualisierungen
mamba install seaborn                    # erweiterte Visualisierungen
mamba install scikit-learn               # statistische Modelle
mamba install pyodbc                     # für Verbindung zwischen Python und SQL Server
mamba install sqlalchemy                 # braucht pyodbc, Für Datenaustausch zwischen Python und SQL Server
```
