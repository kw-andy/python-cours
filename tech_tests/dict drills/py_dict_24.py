def count_letter_dic(inp_str):
    stri = list(inp_str)
    out_dict = {}
    for item in stri:
        if item in out_dict.keys():
            out_dict[item] += 1
        else:
            out_dict[item] = 1
    return out_dict        


print(count_letter_dic('aabcdeartmlqae'))