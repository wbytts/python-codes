
lst = [40, 10, 20, 30]


def min_index(lst):
    return min(range(len(lst)), key=lst.__getitem__)


def max_index(lst):
    return max(range(len(lst)), key=lst.__getitem__)


print(min_index(lst))
print(max_index(lst))
