#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import requests
import re
# 下载小说网页
url = 'http://www.wjsw.com/vip/buyChapter.aspx?cod1&bid=36370&cid=3591807'
# 模拟浏览器发送http请求(get/post)
response = requests.get(url)
# 编码方式
response.encoding = 'utf-8'
html = response.text
# 小说的名字
# title = re.findall(r'<span> (.*?)', html)[0]
# 获取每一章节内容（章节，url）
div = re.findall(r'<div class="vipBox fix>.*?</div>', html, re.S)
chapter_info_list= re.findall(r'id="(.*?)">(.*?)<', div)
# 循环每个章节，分别去下载
for chapter_info in chapter_info_list:
    chapter_url, chapter_title = chapter_info
    chapter_url = "http://www.wjsw.com/vip/buyChapter.aspx?cod1&bid=36370&cid=3591807" % chapter_url

print(chapter_url, chapter_title)
# 下载章节内容
chapter_response = requests.get(chapter_url)
chapter_response.encoding = 'utf-8'
chapter_html = chapter_response.text
# 提取章节内容
chapter_content = re.findall(r'')
