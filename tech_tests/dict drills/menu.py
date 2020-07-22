
def menu(inpt_value):
    menu = {1:"menu 1", 2: "menu 2", 3:"menu 3"}
    try: 
        print(menu[inpt_value])
    except KeyError:
        print("Wrong value")

menu(1)       
menu('bazar') 