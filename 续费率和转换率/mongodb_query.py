#!/usr/bin/python3
import datetime
import time
import pymongo
from myemail import send_email

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['test']
collist = mydb.list_collection_names()
flag =False
if "userinfo" in collist:  # 判断 sites 集合是否存在
    flag =True

else:
    print("集合不存在，请创建后重新启动脚本")
while flag:
    mycol = mydb['userinfo']
    now = datetime.datetime.now()
    delta1 = datetime.timedelta(seconds=30)
    delta2 = datetime.timedelta(hours=8)
    n_days = now - delta1 -delta2
    print(n_days)
    my_query = {"create_time": {"$gt":n_days}}
    for x in  mycol.find(my_query):
        print(x['username'],x['create_time'])
        send_email(x['email'],email_body="%s,欢迎注册"%(x['username']))
    time.sleep(30)