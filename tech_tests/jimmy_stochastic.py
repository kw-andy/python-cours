'''
E-MIAGE D351 - Processus stochastiques et simulation
Devoir 1 Q1 - Pile ou face - vous le programmez
Vous disposez au départ de 100 €.
Vous lancer une pièce:
Si vous avez pile, vous multipliez vos avoirs par 1.5 (ou 150%)
Si vous avez face, vous perdez 40% de vos avoirs (vous les multipliez par 0.6 ou 60%).
Ainsi, par exemple, vous acceptez de jouer, on vous donne les 100 € et vous lancez la pièce.
Vous avez pile, on vous donne 50 € et vous avez désormais 150€.
Vous relancez une pièce, vous avez face. Vous rendez 40% de vos avoirs, soit 60 €, il vous reste donc 90 €.
Vous relancez la pièce et vous avez pile, on vous donne 45 € et vous avez désormais 135 €.
Mettez au point le code python qui permet de simuler le jeu.
Accompagnez votre code d'un affichage simple (sur terminal) qui permet de voir comment évolue le jeu.
Répétez la simulation de manière à calculer une moyenne (du gain, lorsqu'on joue longtemps), et tentez d'évaluer l'écart à cette moyenne.
Jimmy Girard - Mars 2020
'''

 

import numpy
import random
import matplotlib.pyplot as plt
import statistic
from statistics import mean
from statistics import pstdev

def stoch_process(Nb_Simulation,Nb_Lance):

'''
	#Commentaires :

	# pas de é ou à pour les noms de variables, rester sur de l'ascii.
	# Nb_Simulation : Jeu du lancé Pile ou Face - Nombre de simulation(s) - mettre un entier (voir tout à la fin) en lançant 
	  la fonction
	# Nb_Lance : Jeu du lancé Pile ou Face - Nombre de lancé(s) - mettre un entier (voir tout à la fin) - pareil qu'en haut
	# Privélégie les tabulations pour espacer ton code plutôt que des espaces, moins fastidieux à force.
	# a lire : https://www.python.org/dev/peps/pep-0008/ le guide du style pour Python
	
'''



'''

	Commentaires: 
	# pile gain +50% ## tu peux mettre 0.5 ici. Pile = 0.5
	# face perte -40% ## tu peux mettre -0.4 ici Face = -0.4 (est-ce que j'ai mal compris ton code car tu as mis 0.4?)
	# Si la prime est la mise de départ, pourquoi ne pas mettre Prime = 100 et 
		mettre en commentaire 100 car mise de départ
	# TxtMoyenne = '' #si une variable est vide, inutile de l'expliciter en initialisant une variable
	# Les seules variables à expliciter sont les listes comme ListePrime ou les dictionnaires	

'''
	# bloc des variables

	ListePrime = []
	ListeLance = []
	ListeGains = []
	Pile = 50 
	Face = 40 
	PrimeMax = 0
	Prime = 100 
	PileFace = 0
	ListePrime.append(Prime)
	ListeLance.append(0)

'''

	Commentaires: 
	#expliciter les variables comme j ou i, permet d'avoir une meilleure lecture. pour j, tu peux mettre nb_de_simul 
	et pour i, tu peux mettre nb_de_lance
	## avec la correction faite dans le bloc des variables, cela te donnerait  Prime = round(Prime+(Prime * Pile),2) 
	# en re-regardant l'énoncé, tu peux mettre un elif 
	## avec la correction faite dans le bloc des variables, cela te donnerait Prime = round(Prime-(Prime * Face),2) 
	# e

'''	 

'''
	#je ne sais pas si c'est ce que tu souhaitais faire 
	
	for j in range(1,Nb_Simulation +1): 
		for i in range(1,Nb_Lance+1):
			PileFace = random.randint(1,2)
			if  PileFace == 1:
				Prime = round(Prime+(Prime * Pile),2) 
			elif PileFace == 2:
				Prime = round(Prime-(Prime * Face),2) 
			elfif PileFace != 1 and PileFace != 2 : 
			  print('Erreur dans le calcul aléatoire !')
				if Prime > PrimeMax:
			  		PrimeMax = Prime 
			  		ListePrime.append(Prime)
			  		ListeLance.append(i)
			  		ListeGains.append(Prime-MiseDepart)

'''

	for j in range(1,Nb_Simulation +1): 
		for i in range(1,Nb_Lance+1):
			PileFace = random.randint(1,2)
			if  PileFace == 1:
				Prime = round(Prime+(Prime * Pile/100),2) 
			if PileFace == 2:
				Prime = round(Prime-(Prime * Face/100),2) 

			if PileFace != 1 and PileFace != 2 : 
			  print('Erreur dans le calcul aléatoire !')
			if Prime > PrimeMax:
			  PrimeMax = Prime 
			  ListePrime.append(Prime)
			  ListeLance.append(i)
			  ListeGains.append(Prime-MiseDepart)

	   
'''
Commentaires : 

# Je me suis permis de mettre un elif directement
# quand ton texte devient trop long, tu peux mettre un \ pour passer à la ligne
'''
	if Nb_Simulation == 1 :
		print('Montant disponible au départ = ' , MiseDepart , ' €')
		print(' Après ' + str(i) + ' lancé(s) vous disposez de : ' + str(round(Prime,2))+'€' )
		fig = plt.figure(0)
		fig.canvas.set_window_title('Jeu Pile ou Face')
		plt.axis([0, Nb_Lance, 0, PrimeMax+MiseDepart])
		plt.plot(ListeLance,ListePrime )
		plt.title("Evolution des gains")
		plt.xlabel('Nb Lancé(s)'+  ' (Après ' + str(i) + ' lancé(s) vous disposez de : ' + str(round(Prime,2))+'€)' )
		plt.ylabel('Montant en € - (Montant initial = ' + str(MiseDepart) + '€)')
		fig.show()
	elif Nb_Simulation > 1 :
		if mean(ListeGains)>0:
			TxtMoyenne = 'gain'+ ' est de : ' + str(round(mean(ListeGains),2))+'€'
		else :
			TxtMoyenne = 'perte'+ ' est de : ' + str(round(mean(ListeGains),2)*-1)+'€'
		print(' Après ' + str(j) + ' simulation(s) de '+str(i)+ ' lancé(s) avec un montant initial de ' \
			+ str(MiseDepart) + ' € : '+ ' en Moyenne votre ' + TxtMoyenne  + ' avec un Ecart-type de : ' \
			+ str(round(pstdev(ListeGains),2))+'€' )



'''
Commentaires : 

# en faisant comme ci-dessous, tu te permets de lancer ton programme plusieurs fois

'''

stoch_process(3,5) #3 simulations , 5 lancés
stoch_process(2,8) #2 simulations , 8 lancés