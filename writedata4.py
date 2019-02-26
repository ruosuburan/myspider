#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File : writedata.py
# @Author : Shliji
# @Date : ${2019-1-31}
import pymysql
from  sqlalchemy import create_engine

def write_to_sql(tbl, db = 'wade'):
    engine = create_engine('mysql+pymysql://root:******@localhost:3306/{0}?charset=utf8'.format(db))
    # db = 'wade'表示存储到wade这个数据库中,root后面的*是密码
    try:
         tbl.to_sql('listed_company',con = engine,if_exists='append',index=False)
         # 因为要循环网页不断数据库写入内容，所以if_exists选择append，同时该表要有表头，
         # parse_one_page（）方法中df.rename已设置
    except Exception as e:
        print(e)
