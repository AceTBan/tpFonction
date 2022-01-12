# coding=utf-8
import csv


def mail(prenom, nom):
    fprnm = prenom[0][0]
    snom = nom[0]
    return '{}.{}@baton-rouge.fr'.format(fprnm, snom)


def categorie(inscription, annee):
    continuer = True
    while continuer:
        annee.append(input("indique l'annee de naissance de l'adherent\n"))
        try:
            inscription["annee"] = int(inscription["annee"])
        except ValueError:
            print("indiquer l'année en chiffres (AAAA)")
        else:
            continuer = False

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
        print("l'adherent est Non admissible")


def ecrire(fichier, liste):
    with open(fichier, "f") as fiche:
        text = csv.writer(fiche, delimiter="")
        for i in liste:
            text.writerow(i)

# def lire(fichier):
#     with open(fichier, "r") as fiche:
#         for ligne in fiche:
#             print(ligne)
