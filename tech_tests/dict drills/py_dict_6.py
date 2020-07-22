def add_val_dict(*vals):
	the_dict = {}
	for val in vals:
		the_dict[val] = val * val
	return the_dict
	
print(add_val_dict(1,2,3,4,5))		