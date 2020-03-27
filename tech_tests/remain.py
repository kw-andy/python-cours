def giv_back(input_mon : int) ->str:

	dict_notes = {}
	one_or_three = {1 : 'un', 3 : 'trois'}
	
	if input_mon in one_or_three:
		print('impossible de rendre la monnaie car {}'.format(one_or_three[input_mon]))
	elif input_mon % 3 == 1 and input_mon %10 ==3:
		print('impossible de rendre la monnaie car multiple de 3')	
	elif 2 <= input_mon <=10:
		value_test = input_mon % 2
		if value_test == 1:
			number_of_fivers = input_mon // 5 
			dict_notes['fivers'] = number_of_fivers
			remain_mon_by_2 = input_mon % 5
			print(dict_notes)
			if remain_mon_by_2 > 0:
				 dict_notes['two'] = remain_mon_by_2 // 2
				 print(dict_notes)
		else:
			number_of_twoers = input_mon // 2
			dict_notes['two'] = number_of_twoers
			print(dict_notes)
	else:			 
		while input_mon > 1:
			number_of_tenners = input_mon // 10
			dict_notes['ten'] = number_of_tenners
			remain_mon_by_10 = input_mon % 10
			input_mon = remain_mon_by_10
			
			if remain_mon_by_10 >= 5 and remain_mon_by_10 % 2 == 1:
				number_of_fivers = remain_mon_by_10 // 5 
				dict_notes['fivers'] = number_of_fivers
				remain_mon_by_5 = remain_mon_by_10 % 5
				input_mon = remain_mon_by_5
				
				if remain_mon_by_5 == 0:
					print(dict_notes)
					break	
				elif remain_mon_by_5 == 2:
					number_of_twoers = remain_mon_by_5 // 2
					dict_notes['two'] = number_of_twoers
					remain_mon_by_2 = remain_mon_by_5 % 2
					print(dict_notes)
					break
						
			elif remain_mon_by_10 >= 2 and remain_mon_by_10 % 2 == 0:
					number_of_twoers = remain_mon_by_10 // 2
					dict_notes['two'] = number_of_twoers
					remain_mon_by_2 = remain_mon_by_10 % 2
					input_mon = remain_mon_by_2
					print(dict_notes)
					break
			
			print(dict_notes)
			break
					
					


giv_back(255)	
giv_back(777)		
giv_back(988)
giv_back(9)	
giv_back(8)
giv_back(3)
giv_back(253)
giv_back(1)
giv_back(12354)
giv_back(123487654)
giv_back(123457655)
giv_back(10)


'''
input : somme 
output : le nombre de billet en 10, en 5 et de piece de 2
créer un dictionnaire avec le nombre de piece en 2, le nombre de billet en 5 , le nombre de billet en 10
'''				