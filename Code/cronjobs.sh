# kann benutzt werden um automatische Skripte auf Linux zu starten
# jobs gehören zu einem Benutzer und seinen Berechtigungen auf dem Systemm

# Benutzer wechseln
su - username

# zu eigenem Benutzer zurückwechseln
exit

# Liste laufender cronjobs anzeigen (jede Zeile = Cronjob)
crontab -l

# cronjob adden, der jeden Wochentag um 03:00 startet (5 Parameter sind Minute, Stunde, Tag des Monats, Monat, Wochentag
0 3 * * 1-5 /path/to/your/script.sh

# Crojob löschen / ändern im Text Editor
crontab -e

# startet Python code
# startet .sh Datei via Cronjob 
source /home/user/.python_profile # Umgebung setzen
/usr/bin/python3 /path/to/your/script.py --config-filepath /path/to/your/config.yml
