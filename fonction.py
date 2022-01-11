import re


def mail(prenom, nom):
    fprnm= prenom[0][0]
    snom= nom[0]
    return '{}.{}@baton-rouge.fr'.format(fprnm,snom)