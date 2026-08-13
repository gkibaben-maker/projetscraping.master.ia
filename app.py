import sqlite3
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Gaaraas - Voitures d'occasion",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 Gaaraas - Voitures d'occasion")

connexion = sqlite3.connect("gaaraas.db")

df = pd.read_sql_query(
    "SELECT * FROM voitures",
    connexion
)

connexion.close()

st.subheader("📊 Statistiques")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Nombre de voitures",
        len(df)
    )

with col2:
    st.metric(
        "Prix moyen",
        f"{df['Prix'].mean():,.0f} CFA"
    )

with col3:
    st.metric(
        "Kilométrage moyen",
        f"{df['Kilométrage'].mean():,.0f} KM"
    )

st.divider()

st.subheader("🔎 Filtres")

marques = sorted(
    df["Marque"].dropna().unique()
)

marque_selectionnee = st.selectbox(
    "Marque",
    ["Toutes"] + marques
)

boites = sorted(
    df["Boîte de vitesses"].dropna().unique()
)

boite_selectionnee = st.selectbox(
    "Boîte de vitesses",
    ["Toutes"] + boites
)

prix_max = int(
    df["Prix"].max()
)

prix_selectionne = st.slider(
    "Prix maximum (CFA)",
    min_value=0,
    max_value=prix_max,
    value=prix_max,
    step=100000
)

df_filtre = df.copy()

if marque_selectionnee != "Toutes":
    df_filtre = df_filtre[
        df_filtre["Marque"] == marque_selectionnee
    ]

if boite_selectionnee != "Toutes":
    df_filtre = df_filtre[
        df_filtre["Boîte de vitesses"] == boite_selectionnee
    ]

df_filtre = df_filtre[
    df_filtre["Prix"].fillna(0) <= prix_selectionne
]

st.subheader("🚘 Annonces")

st.write(
    f"{len(df_filtre)} voiture(s) trouvée(s)"
)

st.dataframe(
    df_filtre,
    use_container_width=True
)
st.divider()

st.subheader("📊 Boîte de vitesses")

repartition_boite = (
    df_filtre["Boîte de vitesses"]
    .value_counts()
)

st.bar_chart(repartition_boite)
st.subheader("💰 Répartition des prix")

prix_graphique = (
    df_filtre[["Marque", "Modèle", "Prix"]]
    .dropna()
    .sort_values("Prix")
)

st.dataframe(
    prix_graphique,
    width="stretch"
)
st.subheader("🏆 Les 5 voitures les moins chères")

top_5 = (
    df_filtre[
        ["Marque", "Modèle", "Année", "Prix", "Kilométrage"]
    ]
    .dropna(subset=["Prix"])
    .sort_values("Prix")
    .head(5)
)

st.dataframe(
    top_5,
    width="stretch"
)
