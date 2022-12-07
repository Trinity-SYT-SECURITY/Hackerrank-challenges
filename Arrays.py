#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))  # 1 2
    rev = arr[::-1]
    #print(arr[::-1]) [2, 1]
    for element in range(len(rev)):
        print(rev[element], end=' ')  # 2 1
