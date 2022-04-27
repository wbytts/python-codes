def fib_recur(n):
    assert n >= 0
    if n in (0, 1):
        return n
    return fib_recur(n - 1) + fib_recur(n - 2)

for i in range(20):
    print(fib_recur(i), end=" ")
