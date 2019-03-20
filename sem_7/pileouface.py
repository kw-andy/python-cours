"""lancer pile ou face
n fois 
affichage des n résultats

from random import randint

lance = randint('0, 1')

resultat = list(input('résultats : '))"""
from random import randint

lance = int(input('nombre de lancé'))
dico = {}

for ttes_les_valeurs in range(lance):
	dico.update({ttes_les_valeurs : randint(0,1)})

for indexo, lancer in dico.items():
	print('le lancé {} a comme résultats {}'.format(indexo, lancer))

