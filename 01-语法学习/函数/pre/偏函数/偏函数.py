def test(a, b, c, d):
    print(a + b + c + d)


import functools

test2 = functools.partial(test, d=3)

test2(1, 1, 1)
