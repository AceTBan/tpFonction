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

if inscription["annee"] > 2022 - 12:
    print("vous etes Poussin")
elif inscription["annee"] > 2022 - 18:
    print("vous etes Cadet")
elif inscription["annee"] > 2022 - 24:
    print("vous etes Junior")
elif inscription["annee"] > 2022 - 30:
    print("vous etes Semi-pro")
elif inscription["annee"] >= 2022 - 40:
    print("vous etes pro")
else:
    print("Non admis")

mail = input("indiquez votre adresse mail\n")

if fonction.verif_mail(mail):
    print("mail accepter")
else:
    print("mail incorrect")
