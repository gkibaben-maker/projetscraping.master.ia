from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import csv


fichier_csv = "livres.csv"


# ============================================================
# Configuration de Chrome
# ============================================================

options = Options()
# options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)


# ============================================================
# Création du fichier CSV
# ============================================================

with open(
    fichier_csv,
    "w",
    newline="",
    encoding="utf-8"
) as fichier:

    writer = csv.writer(fichier)

    writer.writerow([
        "Titre",
        "Prix",
        "Disponibilité",
        "Nombre_produits",
        "Note",
        "Nombre_reviews",
        "Description",
        "Catégorie",
        "Tax"
    ])

    # ========================================================
    # Parcours des 50 pages
    # ========================================================

    for numero_page in range(1, 51):

        url = (
            f"https://books.toscrape.com/catalogue/"
            f"page-{numero_page}.html"
        )

        driver.get(url)

        print("=" * 60)
        print("PAGE :", numero_page)

        # ----------------------------------------------------
        # Récupération des livres de la page
        # ----------------------------------------------------

        livres = driver.find_elements(
            By.CSS_SELECTOR,
            "article.product_pod"
        )

        nombre_produits = len(livres)

        print("Nombre de produits :", nombre_produits)

        # ----------------------------------------------------
        # IMPORTANT :
        # On récupère toutes les informations de la page
        # AVANT d'aller sur les fiches détaillées.
        # ----------------------------------------------------

        donnees_page = []

        for livre in livres:

            try:
                titre = livre.find_element(
                    By.CSS_SELECTOR,
                    "h3 a"
                ).get_attribute("title")

                lien = livre.find_element(
                    By.CSS_SELECTOR,
                    "h3 a"
                ).get_attribute("href")

                prix = livre.find_element(
                    By.CSS_SELECTOR,
                    ".price_color"
                ).text.strip()

                disponibilite_texte = livre.find_element(
                    By.CSS_SELECTOR,
                    ".availability"
                ).text.strip()

                if "In stock" in disponibilite_texte:
                    disponibilite = "In stock"
                else:
                    disponibilite = "Out of stock"

                note = livre.find_element(
                    By.CSS_SELECTOR,
                    "p.star-rating"
                ).get_attribute("class")

                note = note.replace(
                    "star-rating",
                    ""
                ).strip()

                donnees_page.append([
                    titre,
                    lien,
                    prix,
                    disponibilite,
                    nombre_produits,
                    note
                ])

            except NoSuchElementException:
                continue

        # ====================================================
        # Parcours des fiches détaillées
        # ====================================================

        for donnees in donnees_page:

            titre = donnees[0]
            lien = donnees[1]
            prix = donnees[2]
            disponibilite = donnees[3]
            nombre_produits_page = donnees[4]
            note = donnees[5]

            # ------------------------------------------------
            # Accès à la fiche du livre
            # ------------------------------------------------

            driver.get(lien)

            # ------------------------------------------------
            # V6 - Nombre de reviews
            # ------------------------------------------------

            try:
                nombre_reviews = driver.find_element(
                    By.XPATH,
                    "//th[normalize-space()='Number of reviews']"
                    "/following-sibling::td"
                ).text.strip()

            except NoSuchElementException:
                nombre_reviews = "0"

            # ------------------------------------------------
            # V7 - Description
            # ------------------------------------------------

            try:
                description = driver.find_element(
                    By.CSS_SELECTOR,
                    "#product_description + p"
                ).text.strip()

            except NoSuchElementException:
                description = ""

            # ------------------------------------------------
            # V8 - Catégorie
            # ------------------------------------------------

            try:
                categorie = driver.find_element(
                    By.CSS_SELECTOR,
                    ".breadcrumb li:nth-child(3) a"
                ).text.strip()

            except NoSuchElementException:
                categorie = ""

            # ------------------------------------------------
            # V9 - Tax
            # ------------------------------------------------

            try:
                tax = driver.find_element(
                    By.XPATH,
                    "//th[normalize-space()='Tax']"
                    "/following-sibling::td"
                ).text.strip()

            except NoSuchElementException:
                tax = ""

            # =================================================
            # Écriture dans le CSV
            # =================================================

            writer.writerow([
                titre,
                prix,
                disponibilite,
                nombre_produits_page,
                note,
                nombre_reviews,
                description,
                categorie,
                tax
            ])

            # =================================================
            # Affichage
            # =================================================

            print("Titre :", titre)
            print("Prix :", prix)
            print("Disponibilité :", disponibilite)
            print("Nombre de produits :", nombre_produits_page)
            print("Note :", note)
            print("Nombre de reviews :", nombre_reviews)
            print("Description :", description)
            print("Catégorie :", categorie)
            print("Tax :", tax)
            print("-" * 60)


# ============================================================
# Fermeture du navigateur
# ============================================================

driver.quit()

print("=" * 60)
print("SCRAPING TERMINÉ")
print("Fichier créé :", fichier_csv)
