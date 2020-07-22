def count_success_true(*inpt_dict):
    count = 0
    for key,value in inpt_dict.items():
        if key == 'Success' and value == True:
            count += 1
    return count        


print(count_success_true({'id':1,'Success':True, 'Vintage':False},{'id1':2,'Success':'False','Toto':'Logy'},{'id':235,'Success': True,}))    