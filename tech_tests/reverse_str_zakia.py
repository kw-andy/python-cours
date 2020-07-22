'''
This is probably by far the most common string manipulation interview question. Given an input string, reverse all the words. 

To clarify, 

input: “Interviews are awesome!” 

output: “awesome! are Interviews”. 


Consider all consecutive non-whitespace characters as individual words. If there are multiple spaces between words reduce them to a single white space. Also remove all leading and trailing whitespaces. So, the output for ”   CS degree”, “CS    degree”, “CS degree   “, or ”   CS   degree   ” are all the same: “degree CS”.

'''

print("phrase à modifier")

str = input("tapez votre phrase")

def dev_reverse(str):
	# 1ere action : split
	var_split = str.split()
	#2eme action : 
	var_strip = var_split.strip([])
	#3eme action
	var_reverse = var_strip.reverse()
	#4eme action
	return "".join()
	#"".join(reverse(str.split().strip()))


dev_reverse(str)	
