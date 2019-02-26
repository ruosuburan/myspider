#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File : listed_company.py
# @Author : Shliji
# @Date : ${2019-1-31}
import  pymysql

def generate_mysql():
    conn = pymysql.connect(
        host='localhost',  # 本地服务器
        user='shao',
        password='shliji1998630',  # 你的数据库密码
        port=3306,  # 默认端口
        charset='utf8',
        db='wade')
    cursor = conn.cursor()

    sql='CREATE TABLE IF NOT EXISTS listed_company2 (serial_number INT(30) ' \
        'NOT NULL,stock_code INT(30) ,stock_abbre VARCHAR(30) ,company_name ' \
        'VARCHAR(30) ,province VARCHAR(30) ,city VARCHAR(30) ,' \
        'main_bussiness_income VARCHAR(30) ,net_profit VARCHAR(30) ,' \
        'employees INT(30) ,listing_date DATETIME(0) ,zhaogushu VARCHAR(30) ,' \
        'financial_report VARCHAR(30) , industry_classification VARCHAR(255) ,' \
        'industry_type VARCHAR(255) ,main_business VARCHAR(255) ,PRIMARY KEY (serial_number))'
    # listed_company是要在wade数据库中建立的表，用于存放数据

    cursor.execute(sql)
    conn.close()

    generate_mysql()
