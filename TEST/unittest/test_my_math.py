from unittest import TestCase
from .my_math import MyMath


class TestMyMath(TestCase):

    def setUp(self) -> None:
        print('-' * 100)
        print('创建 MyMath 对象')
        self.mm = MyMath()

    def tearDown(self) -> None:
        print('-' * 100)

    def test_add(self):
        print('测试 MyMath 的 add 方法')
        result = self.mm.add(3, 4)
        self.assertTrue(result == 3 + 4, 'add is error')

    def test_sub(self):
        print('测试 MyMath 的 sub 方法')
        result = self.mm.sub(3, 4)
        self.assertTrue(result == 3 - 4, 'sub is error')
