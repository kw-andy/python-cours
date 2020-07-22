def sort_dic(dic_input):
	sorted_val = {k: v for k ,v in sorted(dic_input.items(), key=lambda item: item[1])}
	return sorted_val


print(sort_dic({1:2 , 2:1 , 3:5, 4:10,5:3}))	

#https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value