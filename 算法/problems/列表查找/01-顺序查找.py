'''
查找：在一些数据元素中，通过一定的方法找出与给定关键字相同的数据元素的过程
列表查找（线性查找）：从列表中查找指定元素
有内置列表查找元素：L.index()

顺序查找，线性查找：从列表第一个元素开始，顺序进行搜索，直到找到元素或搜索到最后一个元素为止
时间复杂度：O(n)
空间复杂度：
'''


def linear_search(lis, val):
    for i, v in enumerate(lis):
        if v == val:
            return i
    return None




