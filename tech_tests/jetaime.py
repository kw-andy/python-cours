'''
def jaimelemacro(poisson):
	poissons = ['thon','lieu','truite']
	assert(poisson in poissons), "macro n'est pas dans la liste de poissons"



try:
	jaimelemacro('macro')
except AssertionError as AssertError:
	print(AssertError)
'''

class coloriage():

	def quellecouleur(self,tteslescouleurs):

		for couleurs in tteslescouleurs:
			print(couleurs)


try:
	lavaria = coloriage()
	lavaria.quellecouleur(1233333)
except:
	print('KO technique')	

		
