# encoding:utf-8
from datetime import datetime

import pymongo
import random
from pymongo_2.random_datetime import random_time

FILE = "order.csv"
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['test']
mycol = mydb['order']
price_dict={1:(399,365,'年卡'),2:(128,90,'季卡'),3:(49,30,'月卡'),4:(19,7,'周卡'),5:(3,1,'日卡'),0:(0,3,'新用户体验')}
state_list = [0,1,2]#0:'待支付',1:'已取消',2:'已支付'
t1 = (2022,1,1,0,0,0,0,0,0)
t2 = (2022,6,27,0,0,0,0,0,0)

for i in range(0,1000):
    date = random_time(t1,t2)
    time = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    insert_dict ={"userid":random.randint(1,500),
                      "product":price_dict[random.randint(0,5)],
                      #"state":state_list[random.randint(0,2)],
                      "state":state_list[2],
                      "pay_time":time,
                  }
    ans = mycol.insert_one(insert_dict)
    print(ans)