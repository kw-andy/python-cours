mot_devin = list(input('tape ton mot à deviner \n'))
soluce = [w.replace(w,'-') for w in mot_devin]
cpteur_erreur = 0
lettre_deja_demande = []


while '-' in soluce:               
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