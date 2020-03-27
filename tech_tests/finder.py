import os



def locate_universe_formula(filename,path):
    # Your code goes here
    for root,dirs,files in os.walk(path):
        if filename in files:
            #print(filename,path)
            return os.path(root)