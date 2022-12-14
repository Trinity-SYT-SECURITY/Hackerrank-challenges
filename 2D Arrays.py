#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':

    arr = []
    sum1 = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    for i in range(4):
        for j in range(4):
            sum1.append(arr[i][j]+arr[i][j+1]+arr[i][j+2] +
                        arr[i+1][j+1]
                        + arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
    print(max(sum1))
# 前行後列[i][j]
# 行列都由0為第一個數
"""
for rows in the array:
      for columns in rows:
    print(columns)

可參考https://www.learncode01.com/python-2d-array/
"""
