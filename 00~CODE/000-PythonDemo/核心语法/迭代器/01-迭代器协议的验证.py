from collections import Iterable, Iterator, Container


class bothIterAndNext:
    def __iter__(self):
        pass

    def __next__(self):
        pass


print('__iter__ 和 __next__ 方法都有，是可迭代的，而且是迭代器')
print(isinstance(bothIterAndNext(), Iterable))  # 两种方法都有的对象是可迭代的
print(isinstance(bothIterAndNext(), Iterator))  # 两种方法都有的对象是迭代器


class onlyNext:
    def __next__(self):
        pass


print('只有 __next__， 不可迭代，不是迭代器')
print(isinstance(onlyNext(), Iterable))  # 只有方法 __next__() 是不可迭代的
print(isinstance(onlyNext(), Iterator))  # 只有方法 __next__() 不是迭代器


class onlyIter:
    def __iter__(self):
        pass


print('只有 __iter__。可以迭代，但不是迭代器')
print(isinstance(onlyIter(), Iterable))  # 只有方法 __iter__() 是可迭代的
print(isinstance(onlyIter(), Iterator))  # 只有方法 __iter__() 不是迭代器
