from prettytable import PrettyTable

def tab_dict(int_dict):
    table = PrettyTable(['key','value'])
    for key,value in int_dict.items():
        table.add_row([key,value])
    return table    


print(tab_dict({1:'a',2:'b',4:'c',5:'d'}))    