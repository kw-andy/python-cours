'''
Consider all consecutive non-whitespace characters as individual words. If there are multiple spaces between words reduce 
them to a single white space. Also remove all leading and trailing whitespaces. 
So, the output for ” CS degree”, “CS degree”, “CS degree “, or ” CS degree ” are all the same: “degree CS”.
'''


def inverse_res(string_words):
	first_res = string_words.split()
	first_res.reverse()
	sec_res = ' '.join(first_res)
	return sec_res

# 1 : trouver comment dérouler les listes en ordre inverse , sans passer par un 
# reverse

# liste[::-1]	

# liste[-1] -> donne le dernier item de la liste

# liste[:-1] -> donne toute la liste sauf le dernier élément