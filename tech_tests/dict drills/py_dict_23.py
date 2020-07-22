def uniq_val(*dict_inp):
    for key,val in dict_inp.items():
        print(key,val)


uniq_val({'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750})        