def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n - 1, a, c, b)
        print('move from %s to %s' % (a, c))
        hanoi(n - 1, b, a, c)


hanoi(10, 'A', 'B', 'C')
