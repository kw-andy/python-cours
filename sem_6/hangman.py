"""
exercice v1 pour le jeu du pendu sur python
"""


#def lettre_dans_mot_a_deviner(lettre,mot_devin):


#a in aba

mot_devin = list(input('tape ton mot à deviner \n')) #le mot défini
soluce = [w.replace(w,'-') for w in mot_devin] #le mot deviné 
cpteur_erreur = 0
lettre_deja_demande = []


while '-' in soluce:        #for , if , while       
	lettre = input('tape ta lettre \n')

	print("Il vous reste encore " + str(8 - cpteur_erreur) + " chances")

	if lettre in lettre_deja_demande:
		print('lettre déjà demandé , choisissez une autre lettre')
	else:
		if lettre in mot_devin:
			for index in range(len(mot_devin)):
				if mot_devin[index] == lettre:
					soluce[index] = lettre
			print('Bonne lettre')
			print(''.join(soluce))

		else:
			cpteur_erreur += 1	
			print('mauvaise lettre')
			print(''.join(soluce))

	lettre_deja_demande.append(lettre)

	if cpteur_erreur == 8:
		break


if cpteur_erreur == 8:
	print("Vous avez perdu")

else :
	print("Vous avez gagné")