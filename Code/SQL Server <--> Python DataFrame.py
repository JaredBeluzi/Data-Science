import pandas as pd
import pyodbc
import sqlalchemy as sa
#import os # nur für environment Variablen

DRIVER = "ODBC Driver 18 for SQL Server"
HOST = "XX.XX.XXX.XXX" 
# HOST kann man so finden:
# finde Servername heraus in SSMS: SELECT @@SERVERNAME AS ServerName
# finde IP-Adresse des Servers über cmd: ping <Servername>
DATABASE = "Ergebnisse"
USER = "user_name"
PASSWORD = "password"  # Du kannst das Passwort lokal laden: os.environ['user_pwd']

engine_url = sa.engine.URL.create(
        "mssql+pyodbc",
        host=HOST,
        username=USER,
        password=PASSWORD,
        database=DATABASE,
        query=dict(driver=DRIVER, TrustServerCertificate='yes') # folgendes adden falls man auf Win arbeitet: Trusted_connection='yes'
    )
engine = sa.create_engine(engine_url, future=True, fast_executemany=True)

# Verbindung über engine testen
with engine.connect() as connection:
    print("Connection successful!")

# Daten importieren
df = pd.read_sql(f"SELECT * FROM S_12345", engine)

# Daten exportieren
df.to_sql('DS_Inflation', con=engine, if_exists='replace', index=False)
