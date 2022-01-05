import re
def verif_mail(adresse):
    rex = re.compile('[A-Z]{1}.[a-z]{7}@baton-rouge.fr')
    if rex.fullmatch(adresse):
        return True
    else:
        return False