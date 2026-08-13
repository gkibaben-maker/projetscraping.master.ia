from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import csv
import time
import re

fichier_csv = "gaaraas.csv"

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

with open(fichier_csv, "w", newline="", encoding="utf-8") as fichier:
    writer = csv.writer(fichier)

    writer.writerow([
        "Marque",
        "Modèle",
        "Année",
        "Prix",
        "Kilométrage",
        "Boîte de vitesses",
        "Région de vente"
    ])

    for numero_page in range(1, 101):
        url = f"https://www.gaaraas.com/fr/users/dakar-auto?page={numero_page}"

        print("=" * 60)
        print("PAGE :", numero_page)

        driver.get(url)
        time.sleep(3)

        annonces = driver.find_elements(
            By.CSS_SELECTOR,
            "a.common-ad-card"
        )

        print("Nombre d'annonces :", len(annonces))

        for annonce in annonces:
            try:
                titre = annonce.find_element(
                    By.CSS_SELECTOR,
                    "h4[title]"
                ).get_attribute("title").strip()

                resultat = re.match(
                    r"(\d{4})\s+(\S+)\s+(.+)",
                    titre
                )

                if resultat:
                    annee = resultat.group(1)
                    marque = resultat.group(2)
                    modele = resultat.group(3)
                else:
                    annee = ""
                    marque = ""
                    modele = titre

                try:
                    prix = annonce.find_element(
                        By.CSS_SELECTOR,
                        ".ad-vehicle-price"
                    ).text.replace("PRIX", "").replace("\n", " ").strip()
                except:
                    prix = ""

                try:
                    kilometrage = annonce.find_element(
                        By.CSS_SELECTOR,
                        ".ad-vehicle-mileage .value"
                    ).text.strip()
                except:
                    kilometrage = ""

                try:
                    boite = annonce.find_element(
                        By.CSS_SELECTOR,
                        ".transmission span"
                    ).text.strip()
                except:
                    boite = ""

                try:
                    region = annonce.find_element(
                        By.CSS_SELECTOR,
                        ".ad-location"
                    ).text.strip()

                    if not region:
                        region = "Dakar"
                except:
                    region = "Dakar"

                writer.writerow([
                    marque,
                    modele,
                    annee,
                    prix,
                    kilometrage,
                    boite,
                    region
                ])

                print("Marque :", marque)
                print("Modèle :", modele)
                print("Année :", annee)
                print("Prix :", prix)
                print("Kilométrage :", kilometrage)
                print("Boîte :", boite)
                print("Région :", region)
                print("-" * 40)

            except Exception as erreur:
                print("Erreur sur une annonce :", erreur)

        print("Page terminée :", numero_page)

driver.quit()

print("=" * 60)
print("SCRAPING GAARAAS TERMINÉ")
print("Fichier créé :", fichier_csv)
