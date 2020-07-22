def rem_keys(dict,key):
	if key in dict:
		del dict[key]
	return dict


print(rem_keys({1:2,2:3,3:55,4:75,5:100},5))	

#https://stackoverflow.com/questions/11277432/how-to-remove-a-key-from-a-python-dictionary