
def empty_dict(dict_inp):
	if len(dict_inp) == 0:
		return 'Empty'
	elif len(dict_inp) > 0:
		return "the len is {}".format(len(dict_inp))

print(empty_dict({1:2,2:3}))
print(empty_dict({}))
