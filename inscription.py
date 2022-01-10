# coding: utf-8
import fonction

inscription = []
nom = []
prenom = []
annee = []

inscrits = int(input("Combien d'adhérent voulez vous saisir ?\n"))

for i in range(inscrits):
    nom.append(input("indiquez le nom de l'adherent\n"))
    prenom.append(input("indiquez le prenom de l'adherent\n"))
    annee.append(input("indique l'annee de naissance de l'adherent\n"))

age = 2022-annee

if age > 12:
    print("vous etes en catégorie Poussin")
elif age > 18:
    print("vous etes en catégorie Cadet")
elif age > 24:
    print("vous etes en catégorie Junior")
elif age > 30:
    print("vous etes en catégorie Semi-pro")
elif age >= 40:
    print("vous etes en catégorie pro")
else:
    print("Non admis")

mail = input("indiquez votre adresse mail\n")

if fonction.verif_mail(mail):
    print("mail accepter")
else:
    print("mail incorrect")
