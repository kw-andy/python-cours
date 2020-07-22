
def rem_dupl(dict_inp):
	result = {}
	for key,value in dict_inp.items():
		if value not in result.values():
			result[key] = value
	return result		


print(rem_dupl({1:2,2:55,3:0,4:78,5:78,6:77,7:378,8:378,9:1000}))	

#https://stackoverflow.com/questions/8749158/removing-duplicates-from-dictionary