#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from threading import Thread
from math import log, sqrt


EPS = .0000001


def sum_func(x):
    summ = x
    prev = 0
    i = 1
    while abs(summ - prev) > EPS:
        prev = summ
        summ += x ** (i * 2 + 1) / (i * 2 + 1)
        i += 1

    print(f"Sum is {summ}")


def check_func(x):
    res = log(sqrt((1 + x) / (1 - x)))
    print(f"Check: {res}")


if __name__ == '__main__':
    x = 0.35
    th1 = Thread(target=sum_func(x))
    th2 = Thread(target=check_func(x))
    th1.start()
    th2.start()
