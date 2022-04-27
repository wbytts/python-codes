def maxfun(x, y):
    max = x
    if (x < y):
        max = y
    return max

result = maxfun(maxfun(3, 5),4)
print(result)
