# -*- coding:utf-8 -*-
import urllib2
import re
import random


#随机生成User-Agent
ua_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
# 爬取www.031ee.com,有跳转
request = urllib2.Request("https://kyfw.12306.cn/otn/leftTicket/init",headers = ua_headers)
response = urllib2.urlopen(request)

html = response.read()

print (html)