def check_key(key_val,dict_input):
	if key_val in dict_input:
		return True
	else:
		return False	

print(check_key(1,{1:2,2:55,3:12}))		

#https://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary