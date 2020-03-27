
#def solution(liste):
#	return len(liste)


# cmt générer tous les sous listes d'une liste ?

def fragments(liste):
	resultat = []
	n = len(liste)
	for i in range(1,n+1):
		for j in range(n-i+1):
			resultat.append(liste[j:j+i])
	return resultat
	
def filter(liste):
	resultat = []
	for els in liste:
		if good(els):
			resultat.append(els)
	return resultat
	


def good(liste):
	resultat = sum(liste)
	return resultat == 0

def solution(liste):
	resultat1 = fragments(liste)
	#print('result1',resultat1)


	resultat2 = filter(resultat1)
	#print('result2',resultat2)

	resultat3 = len(resultat2)

	return resultat3	

#print(solution([2,-2,3,0,4,-7]))

assert solution([2,-2,3,0,4,-7]) == 4

print(solution([2,-2,3,0,4,-7]))


	



# si 0, c'est déjà un ss ens -> on compte 1






# comment déterminer les sous listes qui sont égales à zéro 
## valeurs absolues
