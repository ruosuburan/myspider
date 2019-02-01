#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File : bookreading.py
# @Author : Shliji
# @Date : ${2019-1-31}
import requests
# 下载小说网页
url = 'http://www.wjsw.com/vip/buyChapter.aspx?code=1&bid=36370&cid=3067258'
# 模拟浏览器发送http请求(get/post)
response = requests.get(url)
# 编码方式
response.encoding = 'utf-8'
html = response.text
