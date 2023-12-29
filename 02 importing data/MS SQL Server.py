DRIVER = "ODBC Driver 18 for SQL Server"
HOST = "XX.XX.XXX.XXX"
DATABASE = "Ergebnisse"
USER = "user_name"
PASSWORD = "password"  # you can use os.environ['user_pwd'] to put this part into a local file

engine_url = sa.engine.URL.create(
        "mssql+pyodbc",
        host=HOST,
        username=USER,
        password=PASSWORD,
        database=DATABASE,
        query=dict(driver=DRIVER, TrustServerCertificate='yes')
    )
engine = sa.create_engine(engine_url, future=True, fast_executemany=True)

df = pd.read_sql(f"SELECT * FROM S_12345", engine)
