import csv
import os.path

if not os.path.isfile("inscrits_total.csv"):
    with open("inscrits_total.csv", "i") as fichier:
        texte = csv.DictWriter(file, delimiter="")
        texte.writeheader()