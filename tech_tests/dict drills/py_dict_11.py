def multi_dict(dicts):
	val_final = 1
	for key in dicts:
		val_final = val_final * dicts[key] 
	return val_final


print(multi_dict({1:2,2:3,3:55,4:75,5:100}))	

#https://www.programiz.com/python-programming/methods/dictionary/values