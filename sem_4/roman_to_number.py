"""

function to turn roman to litteral

"""


def input_user():
    return input("entrez un chiffre romain")

def roman_to_number(roman):

    dict = {
        'I': 1,
        'V' : 5,
        'X':10,
        'L': 50,
        }

    resultat = 0

    for i in range(len(roman)) :
        resultat += dict[roman[i]]
        print(resultat)
        if len(roman) > 1 and i != len(roman):
            if roman[i] == 'I' and roman[i+1] != 'I':
                resultat = dict[roman[i+1]] - dict[roman[i]]

    return resultat