# 请求响应
import urllib  # 基础请求库
import requests  # 封装过的好用的第三方请求
# 数据解析
import bs4  # 解析HTML字符串
import re  # 模式匹配
import json # 处理 json 格式的数据
# 数据存储
import openpyxl, xlrd, xlwt, xlutils, xlwings  # 操作 Excel
import sqlite3  # 操作 SQLite 数据库
import redis  # 操作 Redis 数据库
import sqlalchemy # 操作数据库以及ORM映射功能
import pickle  # python 对象持久化
import shelve  # pickle 的封装，通过键存取pickle对象
# 基础支持
import time  # 时间模块
import random  # 随机数模块

base_url = 'https://movie.douban.com/top250?start='

res = urllib.request.urlopen('http://www.baidu.com')

# httpbin.org
print(res.status)
