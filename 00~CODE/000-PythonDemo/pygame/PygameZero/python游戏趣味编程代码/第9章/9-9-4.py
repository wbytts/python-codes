def maxfun(x, y):
    max = x
    if (x < y):
        max = y
    return max

result = maxfun(2, 4)
print(result)
