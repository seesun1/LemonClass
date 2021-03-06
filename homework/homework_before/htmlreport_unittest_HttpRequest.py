import unittest
import time
import HTMLTestRunner
from homework.homework_before.unittest_HttpRequest import TestHttpRequest

class HtmlReporter:
    def __init__(self):
        pass

    def CreateReporter(self):
        suite = unittest.TestSuite()
        suite.addTest(TestHttpRequest('test_get'))
        suite.addTest(TestHttpRequest('test_post'))
        now = time.strftime('%Y-%m-%d_%H_%M_%S')
        # 执行测试集合
        filePath = "pyResult测试报告" + now + ".html"
        fp = open(filePath, 'wb')
        # 生成报告的Title,描述
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Python 测试报告', description='This  is Python  Report')
        runner.run(suite)
        # print(type(runner.run(suite)))
        return filePath

# reporter=HtmlReporter()
# reporter.CreateReporter()