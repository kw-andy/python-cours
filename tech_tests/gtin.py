#12345678 doit renvoyer False
#12345670 doit renvoyer True

def gtin_check(gtin: str)-> str:
	if not isinstance(gtin, str) or len(gtin) not in (8,12,13,14,17,18):
		return 'Not a string'
	else:
		gtin_lst = [int(x) for x in gtin]
		gtin_lst.reverse() # reversing the list as it is easier to work that way
		gtin_original = gtin_lst #saving the list to gtin_original
		gtin_lst = gtin_original[1:] 
		gtin_original.reverse() # reversing back to the original format
		
		# arriving at the algorithm part
		gtin_lst = [x*3 if i%2 == 0 else x for i,x in enumerate(gtin_lst)]
		som_gtin1 = sum(gtin_lst)


		if (som_gtin1 % 10):
			som_gtin2 = som_gtin1 + (10 - som_gtin1 % 10) # (10 // gcd(som_gtin1, 10)) *  som_gtin1 #int(round(som_gtin1, -1)) #som_gtin1 + (10 - som_gtin1 % 10)
		else:	
			som_gtin2 = som_gtin1 
		#print('step 8 : multiple of 10 instead of equal or higher summation',som_gtin2-som_gtin1)

		if (som_gtin2 - som_gtin1) == gtin_original[-1]:
			return True
		else:
			return False	




