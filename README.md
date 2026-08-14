# 🚗📚 Projet Master IA — Web Scraping, Data Engineering et Analyse

## 🎯 Présentation

Ce projet met en place une chaîne complète de collecte, nettoyage, stockage et visualisation de données web.

Deux sources de données sont utilisées :

- 🚗 **Gaaraas** : annonces de voitures d'occasion
- 📚 **Books to Scrape** : catalogue de livres destiné aux exercices de web scraping

Le projet compare également deux approches de collecte :

1. **Selenium** : scraping automatisé avec Python
2. **Web Scraper** : extraction no-code avec l'extension navigateur

La chaîne complète est :

**Scraping → Nettoyage → CSV → SQLite → Analyse → Visualisation Streamlit**
## 🧰 Technologies utilisées

- 🐍 Python
- Selenium
- Pandas
- SQLite
- Streamlit
- Web Scraper
- Git
- GitHub
- VS Code / GitHub Codespaces
## 📊 Sources de données

### 🚗 Gaaraas

Les données Gaaraas concernent des annonces de véhicules d'occasion.

Le scraping Selenium permet d'extraire :

- Marque
- Modèle
- Année
- Prix
- Kilométrage
- Boîte de vitesses
- Région de vente

Résultat :

**245 annonces**

Les données sont disponibles sous plusieurs formes :

- `gaaraas.csv`
- `gaaraas_clean.csv`
- `gaaraas.db`
- `gaaraas-com-2026-08-14.csv`

La base SQLite contient une table `voitures` avec **245 enregistrements**.
### 📚 Books to Scrape

Books to Scrape est utilisé comme deuxième source pour expérimenter le web scraping.

Les données contiennent notamment :

- Titre
- Prix
- Disponibilité
- Nombre de produits
- Note
- Nombre de reviews
- Description
- Catégorie
- Tax

Résultat :

**1 000 livres**

Le fichier nettoyé est :

- `livres.csv`

L'export brut Web Scraper est :

- `books-toscrape-com-2026-08-14-2.csv`
## 🕷️ Scraping avec Selenium

Les scripts Selenium automatisent la navigation et l'extraction des données.

Pour Gaaraas, le script principal est :

`scraping/gaaraas_selenium.py`

Le navigateur Chrome est exécuté en mode headless afin de permettre l'automatisation dans l'environnement GitHub Codespaces.

Les données extraites sont ensuite enregistrées au format CSV et peuvent être nettoyées avec Pandas.
## 🌐 Extraction avec Web Scraper

Le projet utilise également l'extension Web Scraper pour réaliser une extraction sans programmation.

### 🚗 Gaaraas

Résultat :

**245 enregistrements**

Fichier brut :

`gaaraas-com-2026-08-14.csv`

### 📚 Books to Scrape

Résultat :

**1 000 enregistrements**

Fichier brut :

`books-toscrape-com-2026-08-14-2.csv`

Ces exports permettent de comparer les données obtenues avec Web Scraper aux données extraites et nettoyées avec Selenium et Pandas.
## 🧹 Nettoyage des données

Les données extraites sont nettoyées et structurées avec **Pandas**.

Les opérations réalisées permettent notamment de :

- vérifier le nombre d'enregistrements ;
- vérifier les colonnes ;
- nettoyer les données ;
- préparer les données pour l'analyse ;
- enregistrer les données propres au format CSV.

Les principaux fichiers nettoyés sont :

- `gaaraas_clean.csv` → **245 lignes**
- `livres.csv` → **1 000 lignes**
## 🗄️ Base de données SQLite

Les données Gaaraas sont également stockées dans une base SQLite :

`gaaraas.db`

La base contient une table :

`voitures`

avec **245 enregistrements**.

L'application Streamlit utilise cette base pour récupérer les données et réaliser les analyses.
## 📊 Application Streamlit

L'application principale est :

`app.py`

Elle permet de visualiser et d'analyser les données Gaaraas.

### Fonctionnalités

- 📊 Nombre de voitures
- 💰 Prix moyen
- 🚗 Kilométrage moyen
- 🔎 Filtre par marque
- ⚙️ Filtre par boîte de vitesses
- 💵 Filtre par prix maximum
- 📋 Tableau des annonces
- 📊 Répartition des boîtes de vitesses
- 💰 Répartition des prix
- 🏆 Top 5 des voitures les moins chères
- 📥 Téléchargement des données Web Scraper Books
- 📥 Téléchargement des données Web Scraper Gaaraas

Pour lancer l'application :

```bash
streamlit run app.py
## 📁 Organisation du projet

```text
projetscraping.master.ia/
│
├── app.py
├── README.md
├── .gitignore
│
├── gaaraas.db
├── gaaraas.csv
├── gaaraas_clean.csv
├── gaaraas-com-2026-08-14.csv
│
├── livres.csv
├── books-toscrape-com-2026-08-14-2.csv
│
└── scraping/
    └── gaaraas_selenium.py
    ## 📈 Résultats

| Source | Méthode | Nombre d'enregistrements |
|---|---|---:|
| 🚗 Gaaraas | Selenium | 245 |
| 🚗 Gaaraas | Web Scraper | 245 |
| 📚 Books to Scrape | Selenium | 1 000 |
| 📚 Books to Scrape | Web Scraper | 1 000 |

Les différentes méthodes d'extraction permettent de comparer les résultats et de vérifier la cohérence des données.
## 🔄 Architecture du projet

```text
                    INTERNET
                       │
             ┌─────────┴─────────┐
             │                   │
          Gaaraas          Books to Scrape
             │                   │
        ┌────┴────┐         ┌────┴────┐
        │         │         │         │
     Selenium Web Scraper Selenium Web Scraper
        │         │         │         │
        └────┬────┘         └────┬────┘
             │                   │
             ▼                   ▼
        Données brutes      Données brutes
             │                   │
             └─────────┬─────────┘
                       ▼
                     Pandas
                       │
                       ▼
               Données nettoyées
                       │
                  ┌────┴────┐
                  │         │
                 CSV      SQLite
                  │         │
                  └────┬────┘
                       ▼
                   Streamlit
                       │
                       ▼
                  📊 Dashboard
                  ## ▶️ Installation

Créer l'environnement virtuel :

```bash
python -m venv .venv
## ▶️ Lancer l'application

Depuis la racine du projet :

```bash
streamlit run app.py
## 🔍 Vérifications effectuées

Les données ont été vérifiées avec Pandas et SQLite.

### 📚 Books to Scrape

- `livres.csv` → **1 000 lignes**
- Export Web Scraper → **1 000 enregistrements**

### 🚗 Gaaraas

- `gaaraas_clean.csv` → **245 lignes**
- `gaaraas.db` → **245 voitures**
- Export Web Scraper → **245 enregistrements**

Ces vérifications permettent de contrôler la cohérence entre les données extraites, nettoyées et stockées.
## 🚀 Conclusion

Ce projet démontre une chaîne complète de traitement de données web :

**Collecte → Extraction → Nettoyage → Stockage → Analyse → Visualisation**

Il permet également de comparer deux approches de web scraping :

- 🐍 **Selenium** avec Python
- 🌐 **Web Scraper** sans programmation

Le projet constitue une base pour des travaux plus avancés en :

- Data Engineering
- Data Science
- Web Scraping
- Analyse de données
- Bases de données
- Business Intelligence
- Applications Streamlit