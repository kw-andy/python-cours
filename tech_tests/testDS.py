def is_periodic(tokens, period):
    return all(tokens[k] == tokens[k + period] for k in range(len(tokens) - period))


def my_solution(n):
    tokens = f"{n:b}"
    for period in range(1, len(tokens) // 2 + 1):
        if is_periodic(tokens, period):
            return period
    return -1


def solution(n):
    d = [0] * 30
    l = 0
    while n > 0:
        d[l] = n % 2
        n //= 2
        l += 1
        print(d,l,n)
    for p in range(1, 1 + l):
        ok = True
        print('p est ',p)
        for i in range(l - p):
            print('i est ',i)
            if d[i] != d[i + p]:
                ok = False
                break
        if ok:
            return p
    return -1


def range_toto():
    for i in range(100000):
        if solution(i) != my_solution(i):
            print(bin(i), solution(i), my_solution(i))


if __name__ == '__main:__':
    solution()
    my_solution()
