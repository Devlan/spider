# -*- coding:utf-8 -*-
import urllib2
import re
import sys
import random
reload(sys)
sys.setdefaultencoding("utf-8")

# 随机生成User-Agent
USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .\
    NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.5072\
    7)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729\
    ; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; \
    .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.\
    0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3\
    (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/\
    535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]
ua_headers = random.choice(USER_AGENTS)

re_pic_name = re.compile(r"[a-zA-Z0-9]+.jpg")
re_pic_link = re.compile(r"[a-zA-z]+://[^\s]*.jpg")


def write_pic(pic_name, pic_data):
    """
    将读取的网络图片写入本地，并打印图片名
    :param pic_name: 网络图片名
    :param pic_data: 图片二进制数据
    :return:
    """
    pic_full_name = "./av_pics/" + pic_name
    f = open(pic_full_name, 'wb')
    f.write(pic_data)
    f.close()
    print(pic_name)


def get_av_pic():
    soup = ""
    user_input_page = int(raw_input("请输入要下载图片页数:    "))
# 爬取www.509ee.com中文字幕列表图片
    url = "http://www.509ee.com/htm/movielist1/"
    for page in range(1, user_input_page):
        fullurl = url + str(page) + ".htm"
        request = urllib2.Request(fullurl)
        request.add_header("User-Agent", ua_headers)
        response = urllib2.urlopen(request)
        html = response.read()
        pic_name_list = re_pic_name.findall(html)
        pic_link_list = re_pic_link.findall(html)
        for pic_name, pic_link in zip(pic_name_list, pic_link_list):
            pic_request = urllib2.Request(pic_link)
            pic_request.add_header("User-Agent", ua_headers)
            pic_response = urllib2.urlopen(pic_request)
            pic_data = pic_response.read()
            write_pic(pic_name, pic_data)


if __name__ == '__main__':
    get_av_pic()
