def merge_dict(dict1,dict2):
	final_dict = {**dict1,**dict2}
	return final_dict


print(merge_dict({1:2,2:3,3:55},{4:21,5:1}))	


#
#https://stackoverflow.com/questions/38987/how-do-i-merge-two-dictionaries-in-a-single-expression