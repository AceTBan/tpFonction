# coding: utf-8
import fonction
from datetime import*

inscription = []
nom = []
prenom = []

saisie = False

while saisie == False:
    try:
        inscrits = int(input("Combien d'adhérent a saisir ?\n"))
        saisie = True
    except ValueError:
        print("Vous devez entrer un nombre entier")
else:
    continuer = False

for i in range(inscrits):
    nom.append(input("indiquez le nom de l'adherent\n"))
    prenom.append(input("indiquez le prenom de l'adherent\n"))
    fonction.categorie(inscription, annee)

    email = fonction.mail(prenom, nom)
    print("son adresse Email est:", email)

while True:
    perso = input("Avez-vous d'autre inscription ? y/n \n")
    if perso == "n":
        break
    else:
        inscrits


date = str(date.today())
fonction.ecrire("inscrits-" + date + ".csv")
