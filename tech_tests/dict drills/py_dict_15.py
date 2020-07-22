import operator 

def min_max(dict_inp):
	min_val = min(dict_inp.values()) 
	max_val = max(dict_inp.values()) 
	return min_val,max_val


print(min_max({1:2,2:55,3:0,4:78}))	