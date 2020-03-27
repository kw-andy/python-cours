def read_list(inputfile):
	#1ère fonction : prend un fichier pour renvoyer une liste d'entier
	with open(inputfile) as input_file:
		col = [int(line) for line in input_file]
		return col



def test_day_2ble(inputfile):
	col = read_list(inputfile)
	itemdouble = solution(col)
	print(itemdouble)

def solution(col):	
	summ = 0
	dupl_list = [0]

	while True:
		for num in col:
			summ = summ + num
			if dupl_list.count(summ):
				return summ
			dupl_list.append(summ)	

	return 'not found'		
			

test_day_2ble('input_day2.txt')