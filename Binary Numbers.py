#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':

    n = int(input().strip())

    binn = "{0:b}".format(n)
    print(len(list(max(binn.split("0")))))


"""

c = bin(n)[2:]  # bin()返回一個整數int 或者長整數long int 的二進製表示。
 # 不加[2:]的話會輸出0b1100100
    
li = list(c)#100 ['1', '1', '0', '0', '1', '0', '0']

# "{0:b}".format(3)  # Out: '11' “{:b}”用於將參數轉換為二進制形式。

"{1} is the second argument. {0} is the first".format('yellow', 3)
# Out: '3 is the second argument. yellow is the first'

"{1:b}, {0:b}".format(0, 20)  # Out: '10100, 0'
# Note the argument order is switched

0:b 是先把format後的第一個數
https://discuss.codecademy.com/t/string-formatting-query-what-does-0-b-format-num-do/504036/3
"""
