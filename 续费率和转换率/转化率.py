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
mongo_pay_user_objects = mycol.find({'state':2,'product':{'$nin':[[0, 3, '新用户体验']]}}).sort('pay_time')

Time_Delta_1 = datetime.timedelta(days=1)
Time_Delta_7 = datetime.timedelta(days=7)
Time_Delta_15 = datetime.timedelta(days=15)
Time_Delta_30 = datetime.timedelta(days=30)
start_pay_time = datetime.datetime.strptime("2022-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
end_pay_time = datetime.datetime.strptime("2022-06-27 00:00:00", "%Y-%m-%d %H:%M:%S")


def mongdb_find(search_condition_dict):
    """
    根据搜索条件字典返回排序后的搜索结果集
    :param search_condition_dict:查询条件
    :return: 查询结果
    """
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    mydb = myclient['test']
    mycol = mydb['order']
    #dict = {'state': 2}

    return mycol.find(search_condition_dict).sort('pay_time')



def generate_date_dict(search_condition_dict,):
    '''
    根据搜索条件字典调用 mongdb_find，将搜索结果处理成字典返回
    :param search_condition_dict:
    :return: user_dict:键为日期，值为由当日支付完成用户id组成的列表
    '''
    mongdb_find_objects = mongdb_find(search_condition_dict)
    user_dict ={}
    for item in mongdb_find_objects :
        # print(item['pay_time'].strftime("%y-%m-%d"))
        if not item['pay_time'].strftime("%y-%m-%d") in user_dict.keys():
            user_dict[item['pay_time'].strftime("%y-%m-%d")] = []
        user_dict[item['pay_time'].strftime("%y-%m-%d")].append(item['userid'])


    return user_dict

def conversion_count(data_free_time,data_pay_time):
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
            # 遍历当前所求转换率率的日期的免费用户列表，依次取出一一个用户对象为user
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
    # 获取两个数据字典
    data_free_time = generate_date_dict({'state': 2, 'product': [0, 3, '新用户体验']})
    data_pay_time = generate_date_dict({'state': 2, 'product': {'$nin': [[0, 3, '新用户体验']]}})
    # 计算转换率
    conversion_count(data_free_time,data_pay_time)