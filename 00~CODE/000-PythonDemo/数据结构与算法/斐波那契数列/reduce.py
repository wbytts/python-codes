from functools import reduce

fibRe = lambda n: reduce(lambda x, n: [x[1], x[0]+x[1]], range(n), [0, 1])

for i in range(3, 20):
    print(fibRe(i))
