#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    print(arr[::-1])
    rev = arr[::-1]
    for element in range(len(rev)):
        print(rev[element], end=' ')
