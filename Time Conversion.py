#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
  time = s[:8]#取0~8輸入進來的數EX : [08:11:12]
  am_pm = s[8:]#取第八個之後 AM、PM
  h,m,sec = time.splite(':')
  if am_pm == 'PM' and int(h) < 12 :
    h = str(int(h)) + 12)
  elif am_pm == 'AM' and int(h) == 12:
    h = '00'
  return (h+s[2:8])
  #字串 s 若是 "12:34:56PM"。s[2:8] 取得 s 的索引範圍從第2個元素到第8個元素之前（索引7）的部分。這個範圍是 "34:56P"。
  """

當 s = "02:34:56AM" 時，讓我們使用這段程式碼來轉換時間：

time = s[:8]：取得時間部分，time 變成 "02:34:56"。
am_pm = s[8:]：取得上午/下午部分，am_pm 變成 "AM"。
h, m, sec = time.split(':')：將時間部分以冒號分割，h 變成 "02"，m 變成 "34"，sec 變成 "56"。

進入條件判斷：
因為 am_pm 是 "AM" 且 h 是整數 2，不符合 am_pm == 'PM' and int(h) < 12 的條件，也不符合 am_pm == 'AM' and int(h) == 12 的條件，所以不會進入這兩個條件的區塊。
return (h + s[2:8])：將 h（"02"）與 s[2:8]（"34:56A"）結合，最終返回 "02:34:56A"。

所以，輸入 "02:34:56AM" 經過這個程式碼轉換後，輸出為 "02:34:56A"。

  """
  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
