def cache(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper


@cache
def fibR(n):
    if n == 1 or n == 2: return 1
    return fibR(n - 1) + fibR(n - 2)


for i in range(3, 20):
    print(fibR(i))

