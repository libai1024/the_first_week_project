import datetime
import logging
from .log_config import logConfig_usefunction, logConfig_readfile, logConfig_readdict, time_logger

'''
    三种方式配置logging：
    1）使用Python代码显式的创建loggers, handlers和formatters并分别调用它们的配置函数；
    2）创建一个日志配置文件，然后使用fileConfig()函数来读取该文件的内容；
    3）创建一个包含配置信息的dict，然后把它传递个dictConfig()函数；
'''

# #  1）使用Python代码显式的创建loggers, handlers和formatters并分别调用它们的配置函数；
# logger = logConfig_usefunction.create_mylogger()

#  2）创建一个日志配置文件，然后使用fileConfig()函数来读取该文件的内容；
logger = logConfig_readfile.create_mylogger()


# # 3）创建一个包含配置信息的dict，然后把它传递个dictConfig()函数；
# logger = logConfig_readdict.create_mylogger()


logger = time_logger.create_mylogger()

def log(func):
    """
    日志装饰器
    :param func:函数
    """
    def inner(*args,**kwargs):
        logger.info('info message')
        res = func(*args,**kwargs)
        logger.debug(f"func:{func.__name__}{args}->{res}")
        return res
    return inner


import time


# 装饰器
def cal_runtime(func):

    def inner(*args,**kwargs):
        # 时间啜
        start = time.time()  # func开始的时间
        res = func(*args,**kwargs)
        end = time.time()  # func结束的时间
        print("装饰器计算出的时间如下：")
        print(f"{func.__name__} 程序运行的总数时间:{end - start}秒")
        return res
    return inner
