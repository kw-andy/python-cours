def unique_val_dict(dict_inp):
    uniq = set( val for dic in dict_inp for val in dic.values())
    for val in uniq:
        print(val)

unique_val_dict([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}])        