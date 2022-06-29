import datetime

import pymongo
import csv
import codecs

FILE = "order.csv"
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['test']
mycol = mydb['order']



# 续费率= 今日续订人数/上个日订购人数

#{ 第几天：【userid】}

mongo_new_free_user_objects = mycol.find({'state':2,'product':[0, 3, '新用户体验']}).sort('pay_time')
#print(mongo_cirsor_objects)
mongo_pay_user_objects = mycol.find({'state':2}).sort('pay_time')

Time_Delta_1 = datetime.timedelta(days=1)
Time_Delta_7 = datetime.timedelta(days=7)
Time_Delta_15 = datetime.timedelta(days=15)
Time_Delta_30 = datetime.timedelta(days=30)
start_pay_time = datetime.datetime.strptime("2022-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
end_pay_time = datetime.datetime.strptime("2022-06-27 00:00:00", "%Y-%m-%d %H:%M:%S")

start_pay_time.strftime("%y-%m-%d")




data_free_time = {}
data_pay_time = {}

for item in mongo_new_free_user_objects:
    #print(item['pay_time'].strftime("%y-%m-%d"))
    if not item['pay_time'].strftime("%y-%m-%d") in data_free_time.keys():
        data_free_time[item['pay_time'].strftime("%y-%m-%d")] = []
    data_free_time[item['pay_time'].strftime("%y-%m-%d")].append(item['userid'])
print(1,data_free_time)


for item in mongo_pay_user_objects:
    #print(item['pay_time'].strftime("%y-%m-%d"))
    if not item['pay_time'].strftime("%y-%m-%d") in data_pay_time .keys():
        data_pay_time [item['pay_time'].strftime("%y-%m-%d")] = []
    data_pay_time[item['pay_time'].strftime("%y-%m-%d")].append(item['userid'])
print(2,data_pay_time )

def conversion_count():
    conversion_rate ={}
    for period in [1,7,30]:
        flag_time = start_pay_time
        time_delta = Time_Delta_1

        print("model:",period)

        if period == 1:
            time_delta = Time_Delta_1
        elif period == 7:
            time_delta = Time_Delta_7
        elif period == 30:
            time_delta = Time_Delta_30
        while flag_time<end_pay_time:

            count_period_end_time = flag_time + time_delta
            if count_period_end_time > end_pay_time:
                count_period_end_time = end_pay_time
            # 被除数num1
            #print(flag_time)
            if not flag_time.strftime("%y-%m-%d") in data_free_time.keys():
                flag_time = Time_Delta_1 + flag_time
                continue

            num1 = 0
            for user in data_free_time[flag_time.strftime("%y-%m-%d")]:
                current_time = flag_time + Time_Delta_1
                while current_time <= count_period_end_time:
                    if (current_time.strftime("%y-%m-%d") in data_pay_time.keys()) and (user in data_pay_time[current_time.strftime("%y-%m-%d")]):
                        num1 = num1+1
                        break
                    current_time =current_time+Time_Delta_1
            #print(num1)

            # 除数num2
            num2 = len(data_free_time[flag_time.strftime("%y-%m-%d")])
            #print(flag_time,num1,num2)
            if not flag_time in conversion_rate.keys():
                conversion_rate[flag_time]=[]
            conversion_rate[flag_time].append(round(num1/num2,2))
            flag_time=Time_Delta_1+flag_time
        print(conversion_rate)


    import toCsv
    toCsv.toCSV(conversion_rate,'转化率.csv')



if __name__ == '__main__':
    conversion_count()
