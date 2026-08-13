import pandas as pd

df = pd.read_csv("gaaraas.csv")

df["Prix"] = (
    df["Prix"]
    .str.replace("CFA", "", regex=False)
    .str.replace(" ", "", regex=False)
    .str.strip()
)

df["Prix"] = pd.to_numeric(df["Prix"], errors="coerce")

df["Kilométrage"] = (
    df["Kilométrage"]
    .str.replace("KM", "", regex=False)
    .str.replace(" ", "", regex=False)
    .str.strip()
)

df["Kilométrage"] = pd.to_numeric(
    df["Kilométrage"],
    errors="coerce"
)

df["Année"] = pd.to_numeric(
    df["Année"],
    errors="coerce"
).astype("Int64")

df.to_csv(
    "gaaraas_clean.csv",
    index=False,
    encoding="utf-8"
)

print("Nettoyage terminé")
print("Fichier créé : gaaraas_clean.csv")
print("Nombre de lignes :", len(df))
print("Nombre de colonnes :", len(df.columns))
