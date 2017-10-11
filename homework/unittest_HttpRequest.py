#-*-coding:utf-8-*-
import requests
import unittest
import HTMLTestRunner
class Httprequest:
    def __init__(self,ip):
        self.ip = ip
    def get(self,url,data):
        url = self.ip+url
        try:
            rget = requests.get(url,data)
            print('GET的返回测试结果是：',rget.text)
            return rget.text
        except Exception as e:
            print('出错啦！错误参数是：%s'%e)
    def post(self,url,data):
        url = self.ip+url
        try:
            rpost = requests.post(url,data)
            print('POST的返回测试结果是：',rpost.text)
            return rpost.text
        except Exception as e:
            print('出错啦！错误参数是：%s'%e)

url_get = '/futureloan/mvc/api/member/recharge'
data_get = {'mobilephone':'13667692121','amount':1000}
url_post = '/futureloan/mvc/api/member/register'
data_post = {'mobilephone':'13667692121','pwd':'987654321'}

http_re = Httprequest('http://119.23.241.154:8080')
http_re.get(url_get,data_get)
http_re.post(url_post,data_post)