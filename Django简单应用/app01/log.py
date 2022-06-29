import datetime
import logging

logger = logging.getLogger(name=__name__)
logger.setLevel('DEBUG')

formatter = logging.Formatter("%(asctime)s - [%(levelname)s]-%(message)s")

chlr = logging.StreamHandler()

logger.addHandler(chlr)

def log(func):
    """
    日志装饰器
    :param func:函数
    """
    def inner(*args,**kwargs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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
