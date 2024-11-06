from sqlalchemy import create_engine, text

  # Configurația pentru conexiune
conf = {
      'host': "database-1.c3swa08ie01a.eu-north-1.rds.amazonaws.com",
      'port': '3306',
      'user': "admin",
      'password': "agentiesql",
      'database': "proiect"  # Specifică numele bazei de date
  }

  # Creează engine-ul pentru MySQL folosind pymysql
engine = create_engine(
      "mysql+pymysql://{user}:{password}@{host}:{port}/{database}".format(**conf)
  )

  # Execută interogarea și afișează rezultatele
with engine.connect() as conn:
      result = conn.execute(text("SELECT * FROM Tur"))
      rows = result.fetchall()  # preia toate rezultatele
      for row in rows:
          print(row)