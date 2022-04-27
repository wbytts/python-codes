import unittest

from test.unittest.test_my_math import TestMyMath
from test.unittest.unit_test_hello import TestCaseDemo001

# 创建测试套件
test_suite = unittest.TestSuite()
# 获取待测试的用例
test_case_1 = unittest.TestLoader().loadTestsFromTestCase(TestMyMath)
test_case_2 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo001)
# 将用例添加到测试套件中
# test_suite.addTests([test_case_1, test_case_2])
test_suite.addTest(test_case_1)
test_suite.addTest(test_case_2)
# 运行测试套件，并打印测试报告
unittest.TextTestRunner().run(test_suite)
