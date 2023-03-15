import json
def checkCondition(mot):
    majuscule = False
    minuscule = False
    taille8 = False
    chiffre = False
    special = False
    caracteres_speciaux = ['!', '@', '#', '$', '%', '^', '&', '*']

    if len(mot) >= 8:
        taille8 = True

    for lettre in mot:
        if lettre.isupper():
            majuscule = True
        elif lettre.islower():
            minuscule = True
        elif lettre.isdigit():
            chiffre = True
        elif lettre in caracteres_speciaux:
            special = True

    return majuscule, minuscule, taille8, chiffre, special

def getErrorMessage(majuscule, minuscule, taille8, chiffre, special):
    message = ""
    if not majuscule:
        message += "Votre mot de passe doit contenir un caractère majuscule. \n"
    if not minuscule:
        message += "Votre mot de passe doit contenir un caractère minuscule. \n"
    if not taille8:
        message += "Votre mot de passe doit contenir au minimum 8 caractères. \n"
    if not chiffre:
        message += "Votre mot de passe doit contenir au moins un chiffre. \n"
    if not special:
        message += "Votre mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *). \n"

    return message

password = input("Entrez votre mot de passe : ")
while True:
    majuscule, minuscule, taille8, chiffre, special = checkCondition(password)
    if not (majuscule and minuscule and taille8 and chiffre and special):
        error_message = getErrorMessage(majuscule, minuscule, taille8, chiffre, special)
        password = input(f"{error_message}\nEntrez un nouveau mot de passe : ")
    else:
        print("Le mot de passe est valide.")
        break




# with open("password.json", "r") as f:

# with open("password.json", "w") as f:
#
#     data = json.load(f)
#     for password in data["mdp"]:
#         print(password)

