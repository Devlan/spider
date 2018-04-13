# -*- coding=utf-8 -*-


import urllib
import urllib2
#import re



#爬取百度贴吧静态页面
#1.用户输入要爬取的贴吧名称和起止页码
u_tieba_name = raw_input("请输入要爬取的贴吧名字： ")
u_start_page = raw_input("请输入开始页码： ")
u_end_page = raw_input("请输入结束页码： ")

#发送http请求
request = urllib2.Request("http://tieba.baidu.com/")
response = urllib2.urlopen(request)
html = response.read()
print html
