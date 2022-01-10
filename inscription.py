# coding: utf-8
import fonction

inscription = []
nom = []
prenom = []


inscrits = int(input("Combien d'adhérent voulez vous saisir ?\n"))

for i in range(inscrits):
    nom.append(input("indiquez le nom de l'adherent\n"))
    prenom.append(input("indiquez le prenom de l'adherent\n"))
    annee = int(input("indique l'annee de naissance de l'adherent\n"))

age = 2022-annee

if age < 12:
    print("l'adherent en catégorie Poussin")
elif age < 18:
    print("l'adherent en catégorie Cadet")
elif age < 24:
    print("l'adherent en catégorie Junior")
elif age < 30:
    print("l'adherent en catégorie Semi-pro")
elif age <= 40:
    print("l'adherent en catégorie pro")
else:
    print("l'adherent est Non admissible")

mail = input("indiquez votre adresse mail\n")

if fonction.verif_mail(mail):
    print("mail accepter")
else:
    print("mail incorrect")
