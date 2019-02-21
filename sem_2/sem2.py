import turtle,tkinter


"""
creation de la classe.
2 méthodes , une qui fait un carré.
L'autre, fait une mini spirale
"""

class Bouge_Tortue():

	def tortue_carre(self,var1,var2):
		for i in range(var1,var2):
			turtle.forward(50)
			turtle.left(90)
			

	def tortue_mini_spirale(self,debu1,debu2):
		turtle.shape("turtle")
		for pas in range(debu1,debu2,2):
			turtle.forward(pas)
			turtle.right(pas)
			
"""
# tout le code ci-dessous est fait pour faire comprendre 
# l'instantiation, entre autres, et comment cette instantiation peut-être utilisé 
# dans une boucle.

# le shape permet d'avoir un format de tortue 

turtle.shape("turtle")

# instantiation de la classe
			
varia1 = Bouge_Tortue()


# on utilise les deux méthodes , pour avoir une automatisation de dessin.
# Pour info, chaque nouveau dessin commence là ou finit l'ancien.


for cpte in range(0,5):
	varia1.tortue_carre(0,4)
	varia1.tortue_mini_spirale(0,100)	
	
"""	
