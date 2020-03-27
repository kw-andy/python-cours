def is_periodic(tokens, period):
    return all(tokens[k] == tokens[k + period] for k in range(len(tokens) - period))


def my_solution(n):
    tokens = f"{n:b}"
    for period in range(1, len(tokens) // 2 + 1):
        if is_periodic(tokens, period):
            return period
    return -1


def solution(theinput):
    list_chain = [0] * 30
    incrementor = 0
    while theinput > 0:
        list_chain[incrementor] = theinput % 2
        theinput //= 2
        incrementor += 1
        print(list_chain,incrementor,theinput)
    for elts in range(1, 1 + incrementor//)2:
        ok = True
        print('elts est ',elts)
        for oth_elts in range(incrementor - elts):
            print('oth_elts est ',oth_elts)
            print(list_chain[oth_elts],list_chain[oth_elts + elts])
            if list_chain[oth_elts] != list_chain[oth_elts + elts]:
                print('break here',list_chain[oth_elts],list_chain[oth_elts + elts])
                ok = False
                print(ok)
                break
        if ok:
            print(ok)
            return elts
    return -1


def range_toto():
    for i in range(100000):
        if solution(i) != my_solution(i):
            print(bin(i), solution(i), my_solution(i))


if __name__ == '__main:__':
    solution()
    my_solution()
