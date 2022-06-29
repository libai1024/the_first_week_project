import time
import random


def random_time(t1,t2):
    start_time =time.mktime(t1)
    end_time = time.mktime(t2)
    t = random.randint(start_time,end_time)
    date_touple = time.localtime(t)
    date = time.strftime("%Y-%m-%d %H:%M:%S",date_touple)
    return date
