f = lambda n: 1 if n in (1, 2) else f(n-1) + f(n-2)

for i in range(3, 20):
    print(f(i))
