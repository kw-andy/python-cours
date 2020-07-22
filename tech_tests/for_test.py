def run_for(elts):
    for elt in elts:
        print(elt, end=",")

run_for([1,2,3,4,5,6,7,8,9,10,11])

'''

In Python 3.6+ it actually has an added thing that the repetitions happen at the first occurrence:
  
>>> ''.join(collections.Counter('Antti Haapala').elements())
'Antti Haaaapl'
Same applies to keys naturally
>>> ''.join(collections.Counter('Antti Haapala').keys())
'Anti Hapl'

'''