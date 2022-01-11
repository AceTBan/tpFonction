# coding: utf-8
import fonction

inscription = []
nom = []
prenom = []
annee = []

saisie=False

while saisie==False:
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

    continuer = True
    while continuer:
        annee.append(input("indique l'annee de naissance de l'adherent\n"))
        try:
            inscription["annee"] = int(inscription["annee"])
        except ValueError:
            print("indiquer l'année en chiffres (AAAA)")
        else:
            continuer = False

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

# while True:
#     perso = input("Avez-vous d'autre inscription ? y/n \n")
#     if perso == "n":
#         break
#     else:                 (essayer de mettre la saisi de l'adhérent dans fonction.py afin de l'appeler ici-