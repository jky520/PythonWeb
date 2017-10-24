# _*_ coding:utf-8 _*_
__author__ = "@DT人"

import urllib.request # 爬虫模块或网页访问模块,python3的写法：urllib.request
import re

def getSortList():
    response = urllib.request.urlopen('http://www.quanshuwang.com/list/1_1.html')
    html = response.read() # 返回为gbk
    html = html.decode('gbk')  # 解码decode 为 unicode
    html = html.encode('utf-8') #编码encode，将unicode转换成utf-8 

    reg = r'<a target="_bank" title="(.*?)" "href="(.*?)" class="clearfix stitle">(.*?)</a>'
    return re.findall(reg, html)[0]

def getNoverList(url):
    html = urllib.request.urlopen(url).read.decode('gbk').encode('utf-8')
    reg = r'<li><a href="(.*?)" title="(.*?)"></a></li>'
    chapterList = re.findall(reg, html)
    return chapterList

def getNoverUrl():
    pass

def getChapterContent(url):
    html = urllib.request.urlopen(url).read.decode('gbk').encode('utf-8')
    reg = r'style5\(\);</script>(.*?)<script type="text/javascript">'
    reg = re.compile(reg,re.S)
    return re.compile(reg, html)[0]


for name, url in getSortList():
    print(name,url)
    # noverUrl = getNoverContent(url)
    # for chapterUrl,chapterName in getNover
