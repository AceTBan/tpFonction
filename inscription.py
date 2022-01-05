# coding: utf-8
import re

nom = input("indiquez votre nom \n")
prenom = input("indiquez votre prenom \n")
annee = int(input("indique votre annee de naissance \n"))


def verif_mail(adresse):
    rex = re.compile('[A-Z]{1}.[a-z]{7}@baton-rouge.fr')
    if rex.fullmatch(adresse):
        return True
    else:
        return False


if annee > 2022 - 12:
    print("vous etes Poussin")
elif annee > 2022 - 18:
    print("vous etes Cadet")
elif annee > 2022 - 24:
    print("vous etes Junior")
elif annee > 2022 - 30:
    print("vous etes Semi-pro")
elif annee >= 2022 - 40:
    print("vous etes pro")
else:
    print("Non admis")

mail = input("indiquez votre adresse mail\n")

if verif_mail(mail):
    print("mail accepter")
else:
    print("mail incorrect")
