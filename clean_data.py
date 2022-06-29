# encoding:utf-8
import datetime

import pymongo
import csv
import codecs

print(type(datetime.datetime.now().month))
FILE = "order.csv"
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['test']
mycol = mydb['order']


for i in range(1,251):
    # 1、免费试用仅限一次，去多余
    count = 0
    mongo_free_try_delete = mycol.find({'userid': i,'state':2, 'product':[0, 3, '新用户体验']}).skip(1)
    for item in mongo_free_try_delete:
        res = mycol.delete_one(item)
        print(res)




