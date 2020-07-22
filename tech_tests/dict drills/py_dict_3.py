def merge_dict(*dicts):
	final_dict = {}
	for dict in dicts:
		final_dict.update(dict)
	return final_dict
	
print(merge_dict({1:2, 2:3,3:5},{4:13}))		

#https://stackoverflow.com/questions/1781571/how-to-concatenate-two-dictionaries-to-create-a-new-one-in-python

