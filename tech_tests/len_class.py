class cptage:

	def __init__(self,miaou):
		self.miaou = miaou


	def __len__(self):
		return len(self.miaou)

print(len(cptage([1,2,3,4,5,7,8,9,0])))

#compt.miaou = [1,2,3,4,5] and then do print(len(compt)) 



#len(compt([1,2,3,4,5]))		


class cptage:

	def __init__(self,miaou):
		self.miaou = miaou

	def __call__(self):
		return self.miaou	

	def __len__(self):
		return len(self.miaou)

compt = cptage([1,2])

print(len(compt([1,2,3])))


#print(len(compt))
