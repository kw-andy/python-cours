
def permut_dic(inp_dic):
    val_list = []
    for ke,va in inp_dic.items():
        val_list.append(va)
        res = [[item[0],item1[1]] for item in val_list for item1 in val_list]
    return res

print(permut_dic({'1':['a','b'], '2':['c','d']}))    

''' solution for that one
import itertools      
d ={'1':['a','b'], '2':['c','d']}
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo))
'''