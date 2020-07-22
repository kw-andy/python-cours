'''
The most basic part for inheritance: use the self in the method
'''

class A:

    def print_toto(self):
        print("Yo, what's up?")

class B(A):
    pass

xyz= B()

xyz.print_toto()

'''
A more detailed class variation with the self variable
'''


class A():

    def __init__(self,name):
        self.name = name

    def test_print(self):
        print("This is A's",self.name)

class B(A):
    pass

x = B("jason")

x.test_print()
