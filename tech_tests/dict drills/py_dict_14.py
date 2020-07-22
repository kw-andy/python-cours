def sort_keys(list_inp):
	
	final_dict = {}
	'''
	for key,value in list_inp.items():
		print(key,value)
		#final_dict[key] = value 
	'''
	trie = dict(list_inp.items().sorted()) 
	return trie



print(sort_keys({1:3,3:5,2:3,5:55,4:3}))	

#sort_keys({1:3,3:5,2:3,5:55,4:3})

#https://stackoverflow.com/questions/209840/convert-two-lists-into-a-dictionary