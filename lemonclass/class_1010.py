import unittest
from lemonclass.class_928课堂练习 import Math
from parameterized import parameterized

class TestMath(unittest.TestCase):

     # @parameterized.expand([
     # ("第一条",1,1,2),
     # ("第二条",2,2,4),
     # ("第三条",3,3,6),
     # ])

     def setUp(self):
         pass

     def test_sum(self,a=5,b=5,c=10):
         t=Math(a,b)
         result1=t.sum()
         self.assertEqual(result1,c,"加法报错")
         # print("测试数据是",name)

     def test_sub(self,a=5,b=5,c=10):
         s=Math(c,b)
         result2=s.sub()
         self.assertEqual(result2,a,"减法报错")
         # print("测试数据是", name)

     def tearDown(self):
         pass


if __name__ =='__main__':
        unittest.main()


