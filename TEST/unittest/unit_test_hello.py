import unittest  # python 中的单元测试套件，类似Java的JUnit


class TestCaseDemo001(unittest.TestCase):

    def setUp(self) -> None:
        print('-' * 100)
        print('setUp，在每个测试方法之前执行......')

    def tearDown(self) -> None:
        print('tearDown，在每个测试方法之后执行')
        print('-' * 100)

    def show(self):
        print('此方法不会执行测试')

    def test001(self):
        print('以test开头的方法，可以运行')
        self.assertTrue(1 + 1 == 2, 'test001 is error')


if __name__ == '__main__':
    unittest.TestCase()
