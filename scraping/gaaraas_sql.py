import sqlite3
import pandas as pd

csv_file = "gaaraas_clean.csv"
db_file = "gaaraas.db"

df = pd.read_csv(csv_file)

connexion = sqlite3.connect(db_file)

df.to_sql(
    "voitures",
    connexion,
    if_exists="replace",
    index=False
)

connexion.close()

print("Base SQL créée")
print("Fichier :", db_file)
print("Table : voitures")
print("Nombre de lignes :", len(df))
