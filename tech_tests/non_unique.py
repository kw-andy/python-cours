'''
This question demonstrates efficient use of hashtable. 
We scan the string from left to right counting the number occurrences 
of each character in a hashtable. Then we perform a second pass 
and check the counts of every character. 
Whenever we hit a count of 1 we return that character, 
that’s the first unique letter. If we can’t find any unique characters, 
then we don’t return anything (None in python). Here’s the code:

'''

def unique_occ(the_str: str)->str:
	res1 = list(the_str)
	unique_letter = []
	non_unique = []
	for i in res1:
		if i not in unique_letter:
			unique_letter.append(i)
		else:
			non_unique.append(i)
	unique_sort = [elts for elts in unique_letter if elts not in non_unique]
	non_unique1 = [elts for elts in unique_letter if elts in non_unique]
	non_unique = non_unique + non_unique1
	non_unique2 = {i:non_unique.count(i) for i in non_unique}
	return 'unique letter is {} and non unique letter is {}'.format(unique_sort,non_unique2)


'''
a more pythonic way
'''			

def unique_letters(string: str)-> str:
	letters = Counter(string)
	unique = [key for key in letters if letters[key]==1]
	non_unique= {key : letters[key] for key in letters if letters[key] >1}
	return f"Unique: {unique} | Not unique: {non_unique}"
