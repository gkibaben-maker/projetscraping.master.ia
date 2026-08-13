# Projet de Web Scraping — Gaaraas & Books

## 🎯 Objectif

Projet individuel de web scraping réalisé avec Python. Le projet collecte des données depuis des sites web, les nettoie, les stocke dans une base SQL et les présente dans une application Streamlit.

## 🛠️ Technologies utilisées

- Python
- Selenium
- Pandas
- SQLite
- Streamlit
- CSV

## 🕷️ 1. Scraping

Le scraping des annonces automobiles de Gaaraas est réalisé avec Selenium.

Les données collectées sont :

- Marque
- Modèle
- Année
- Prix
- Kilométrage
- Boîte de vitesses
- Région de vente

Le fichier brut généré est .

Un second scraper Selenium permet également de collecter des données de livres dans .

## 🧹 2. Nettoyage des données

Les données Gaaraas sont nettoyées avec Pandas.

Les prix et les kilométrages sont convertis en valeurs numériques afin de faciliter leur analyse.

Le fichier nettoyé est :



## 🗄️ 3. Base de données SQL

Les données nettoyées sont importées dans une base SQLite :



La table principale est :



La base contient 245 annonces automobiles.

## 📊 4. Application Streamlit

L'application  permet de consulter et analyser les données.

Elle affiche notamment :

- le nombre de voitures ;
- le prix moyen ;
- le kilométrage moyen ;
- des filtres par marque ;
- des filtres par boîte de vitesses ;
- un filtre par prix maximum ;
- la répartition des boîtes de vitesses ;
- les prix triés ;
- les 5 voitures les moins chères.

## 🚀 Installation

Créer et activer un environnement virtuel, puis installer les dépendances :



## ▶️ Lancer l'application

Depuis la racine du projet :



## 📁 Organisation du projet



## ✅ Résultat

Le projet met en place une chaîne complète :

**Scraping → Nettoyage → SQL → Analyse → Visualisation Streamlit**
