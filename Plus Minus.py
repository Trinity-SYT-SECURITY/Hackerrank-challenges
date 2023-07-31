# 這題需要在6個數字中找出正、負、0占比，將其轉換成小數並算到第六位
# 如果是[2,2,-1,0,5,-3]，正數佔3/6換成小數為0.500000，以此類推
import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
  positive = 0
  negative = 0
  zeros = 0
  for i in arr:#遍歷陣列數
    if i > arr:
      positive+=1
    elif i == 0:
      zeros+=1
    elif i < arr:
      negative+=1
  print("{:.6f}".format(positive/n))
  print("{:.6f}".format(negative/n))
  print("{:.6f}".format(zeros/n))
    
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
