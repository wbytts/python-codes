import numpy


def fib_matr(n):
    return (numpy.matrix([[1, 1], [1, 0]]) ** (n - 1) * numpy.matrix([[1], [0]]))[0, 0]


for i in range(200):
    print(int(fib_matr(i)))
