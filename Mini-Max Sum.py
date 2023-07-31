#陣列中的數值相加，每次都減掉一個數字去計算總合，最後求總合的組合中最大跟最小數
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
  print(sum(arr)-max(arr),sum(arr)-min(arr),sep=' ')#總數扣最大數為最小值，總數扣最小數為最大值
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
