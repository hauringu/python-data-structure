# -*- coding: utf-8 -*- 
# @Time : 2021/3/16 17:49 
# @Author : HGuoo 
# @File : cal_time.py


import time


def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time : %s secs." % (func.__name__, t2 - t1))
        return result

    return wrapper
