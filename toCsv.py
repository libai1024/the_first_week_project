# encoding:utf-8
import datetime

import pymongo
import csv
import codecs

def toCSV(datas,FILE = "order.csv",):

    with codecs.open(FILE, 'w+', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # 设置csv头行，选择要导出的字段
        #["时间", "续费率"]
        writer.writerow(["日期","日续费率","周续费率","月续费率"])
        start_pay_time = datetime.datetime.strptime("2022-01-01", "%Y-%m-%d")
        #print(datas)
        for key in datas:
             writer.writerow([datetime.datetime.strftime(key, "%Y-%m-%d")
                             ,str(datas[key][0])
                             ,str(datas[key][1])
                             ,str(datas[key][2])])