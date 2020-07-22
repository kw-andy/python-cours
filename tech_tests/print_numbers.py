def print_numbers(num):
    for nu in range(1,num):
        if is_even(nu):
            print('{} is even'.format(nu))
        else:
            print('{} is odd'.format(nu))    

def is_even(num):
    return num % 2 == 0    


print_numbers(50)    