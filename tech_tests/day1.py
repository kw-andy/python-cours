def sum_file(inputfile):
	with open(inputfile) as input_file:
		col = [int(line) for line in input_file]
		summ = 0
		length = len(col)
	print(col)
	print(length)
	for num in col:
		print(num)
		summ = summ + num
		print(summ)	
	'''
	for num in range(length):
		#print(num)
		summ = summ + num
		print(summ)
		return summ
	'''