def comm_keys(dict1,dict2):
    for key in dict1:
        if key in dict2:
            dict2[key] = dict2[key] + dict1[key]
        else:
            pass

    return dict2        

print(comm_keys({1:23,2:23,33:5},{1:23,2:55,233:5,5:23}))    


#https://www.geeksforgeeks.org/python-combine-two-dictionary-adding-values-for-common-keys/