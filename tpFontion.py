import re
nom = input("indiquez votre nom")
prenom = input("indiquez votre prenom")
annee = int(input("indique votre annee de naissance"))
mail = input("indiquez votre adresse mail\n")

if annee > 2016:
    print("vous etes Poussin")
elif annee > 2010:
    print("vous etes Cadet")
elif annee > 2004:
    print("vous n'etes pas majeur")
elif annee > 1998:
    print("vous etes Junior")
elif annee > 1992:
    print("vous etes Semi-pro")
elif annee >= 1982:
    print("vous etes pro")
else:
    print("Non admis")

def verif_mail(adresse):
    rex = re.compile("[A-Za-z0-9]{4}@[A-Za-z0-9]{6}\.[A-Z|a-z]{3}")
    if rex.fullmatch(adresse):
        return True
    else:
        return False

def verif_mail_long(adresse):
    if adresse[2] != "." or adresse[11] != "@":
        return False
    for ind, val in enumerate(adresse):
        if (ind < 2) or (ind >= 1 and ind <= 10) or ind > 11:
            if not val.isalnum():
                return False
    return True

if verif_mail_long(mail):
    print("OK")
else:
    print("KO")