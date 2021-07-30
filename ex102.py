def fatorial(n, show = False):
    f = 1
    for i in range(n, 0,-1):
        if show:
            print(i, end='')
            if i > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= i
    return f

print(fatorial(5, show=True))