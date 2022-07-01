import datetime

import pymongo
import csv
import codecs



Time_Delta_1 = datetime.timedelta(days=1)
Time_Delta_7 = datetime.timedelta(days=7)
Time_Delta_15 = datetime.timedelta(days=15)
Time_Delta_30 = datetime.timedelta(days=30)
start_pay_time = datetime.datetime.strptime("2022-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
end_pay_time = datetime.datetime.strptime("2022-06-27 00:00:00", "%Y-%m-%d %H:%M:%S")
data_pay_time = {}


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

    # print(user_dict)
    return user_dict


def renewrate_count(data_pay_time):
    '''
    根据数据字典计算出续费率，并生成csv文件
    :param data_pay_time: 键为付费日期的字典
    :return: None
    '''

    # 续费率字典集
    global one_period_time
    renew_rate ={}

    # 遍历列表，对每日、每周、每月付费率进行计算。
    for period in [1,7,30]:
        flag_time = start_pay_time
        time_delta = Time_Delta_1

        print("model:",period)

        #  one_period_time 一个统计周期时间
        if period == 1:
            one_period_time = Time_Delta_1
        elif period == 7:
            one_period_time = Time_Delta_7
        elif period == 30:
            one_period_time = Time_Delta_30

        # flag_time 为当前所求续费率的日期，通过while实现对整个时间段 续费率的计算
        while flag_time<end_pay_time:
            #  count_period_end_time 计算该统计周期的结束是哪一天
            count_period_end_time = flag_time +  one_period_time
            # 如果统计周期结束时间比 该时间段最后一天还短，则赋值为时间段的最后一天
            if count_period_end_time > end_pay_time:
                count_period_end_time = end_pay_time


            # 计算被除数num1
            # 如果当前所求续费率的日期不在数据字典的键中，则用于规定临界条件的变量flag_time 前移一天并跳过当前循环
            if not flag_time.strftime("%y-%m-%d") in data_pay_time.keys():
                flag_time = Time_Delta_1 + flag_time
                continue
            num1 = 0
            # 遍历当前所求续费率的日期的付费用户列表，依次取出一一个用户对象为user
            for user in data_pay_time[flag_time.strftime("%y-%m-%d")]:
                current_time = flag_time + Time_Delta_1
                # while循环遍历到统计周期结尾那一天，如果当天存在user用户，则num1+1,且跳出循环
                while current_time <= count_period_end_time:
                    if (current_time.strftime("%y-%m-%d") in data_pay_time.keys()) and (user in data_pay_time[current_time.strftime("%y-%m-%d")]):
                        num1 = num1+1
                        break
                    current_time =current_time+Time_Delta_1
            #print(num1)

            # 除数num2 为当天付费人数，即列表长度
            num2 = len(data_pay_time[flag_time.strftime("%y-%m-%d")])
            #print(flag_time,num1,num2)
            if not flag_time in renew_rate.keys():
                renew_rate[flag_time]=[]
            renew_rate[flag_time].append(round(num1/num2,2))
            flag_time=Time_Delta_1+flag_time
        print(renew_rate)

    # 生成csv文件
    import toCsv
    toCsv.toCSV(renew_rate,'续费率.csv')


if __name__ == '__main__':
    # 先获取数据字典
    data_pay_time = generate_date_dict({'state':2})
    # 处理数据 计算续费率
    renewrate_count(data_pay_time)

