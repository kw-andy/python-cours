class kdo_pack():

	def __init__(self, maxsledge = 12, remainingplace=0):
		self.maxsledge = maxsledge
		self.remainingplace = remainingplace
		self.giftlist = []

	def gift_type(self,size_gift):
		#size_gift: {1: "une demi seconde",2: "un seconde",3: "deux secondes"}
		#if 1 in size_gift:
		#	return "une demi seconde"
		#elif 2 in size_gift:
		#	return "une seconde"
		#elif 5 in size_gift:
		#	return "deux secondes"	
		return {1: 'half second', 2: 'one second', 3:'three secs'}[i]	#Voir avec Colin

	def Dwarf(self):
		while self.remainingplace < self.maxsledge:
			self.size_gift = int(input("type the size, 1 (for 1kg),2 (for 2kg) or 5 (for 5 kg) \n"))
				
			temps = self.gift_type(self.size_gift)
			print('It will take me ',temps, ' because the size of the gift is  {} kg'.format(self.size_gift))

			self.remainingplace += self.size_gift
			#return self.remainingplace
			self.giftlist.append(self.size_gift)
			print(self.remainingplace)
			print(self.giftlist)


	def Reindeer(self):
		print("list of gift is the following : ",self.giftlist)		
		self.printcounter = len(self.giftlist)
		#print(self.printcounter)
		#print(len(self.giftlist))

		while self.printcounter > 0:			
			if self.printcounter %5 == 0:
				print(self.printcounter)
				print("I stop, give me reindeer milk !")
				break
			else:
				self.giftlist.remove(self.giftlist[0])	
				self.printcounter-=1
				#print("there are only {} gifts to deliver".format(self.printcounter))
				print(f"there are {len(self.giftlist)} gift(s) left to deliver")





test123 = kdo_pack()
test123.Dwarf()
test123.Reindeer()


'''

Bon t'as tout mis dans une classe, moi je ne suis pas hyper fan de ça (mas balek car il y a peu de code) ca fait un peu javaesque.


Ensuite il a des soucis de casse (genre les fonctions toussa)

ta fonction gift_type pourrait etre pls pythonnique avec un dico


return {1: 'half second', 2: 'one second'}[i]


moi j'aurai utilisé 's' 'm' et 'l' plutot que 1, 2,3


le coup de la panne t'aurais pu le faire avec random mais bon ... balek

tu peux while self.printcounter:


tu peux meme while self.giftlist en fait


tu peux utiliser les f-string


print(f"there are {len(self.giftlist)} gift(s) left to deliver")


Au niveau de la logique "metier" faut faire gaffe avec trois cadeaux de 5 kg tu dépasses les 12


ton remaining induit en erreur ce n'est pas la place qui reste mais la place qui est occuée
'''