

def high_val(input_dict):
    res = []
    for key,val in input_dict.items():
        #print(val)
        res.append(val)
        res_fin = sorted(res,reverse=True)
    return res_fin[0:3]

print(high_val({1:2,2:3,3:5,4:5,5:23,5:345}))        
