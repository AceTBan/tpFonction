# coding: utf-8
import fonction

inscription = []
nom = []
prenom = []

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
<<<<<<< HEAD

    continuer = True
    while continuer:
        annee.append(input("indique l'annee de naissance de l'adherent\n"))
        try:
            inscription["annee"] = int(inscription["annee"])
        except ValueError:
            print("indiquer l'année en chiffres (AAAA)")
        else:
            continuer = False
=======
    annee = int(input("indique l'annee de naissance de l'adherent\n"))
>>>>>>> 79bf27df232eb0d2099aab552f57b7efeec9cf25

age = annee - 2022

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
<<<<<<< HEAD
    print("mail incorrect")

# while True:
#     perso = input("Avez-vous d'autre inscription ? y/n \n")
#     if perso == "n":
#         break
#     else:                 (essayer de mettre la saisi de l'adhérent dans fonction.py afin de l'appeler ici-
=======
    print("l'adherent est Non admissible")

email = fonction.mail(prenom, nom)
print("son adresse Email est:",email)
>>>>>>> 79bf27df232eb0d2099aab552f57b7efeec9cf25
