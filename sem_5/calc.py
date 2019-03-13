def calculatrice():
     chif1 = input('tape ton 1er chiffre \n')
     ope = input('tape ton opé \n')
     chif2 = input('tape ton 2ème chiffre \n')
     if ope == '+':
         print(int(chif1) + int(chif2))
     elif ope == '-':
         print(int(chif1) - int(chif2))
     elif ope == '*':
         print(int(chif1) * int(chif2))
     elif ope == '/':
         print(int(chif1) / int(chif2))
