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
            print(arr[i][j])
    print(max(sum1))
