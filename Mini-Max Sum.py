#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    aMin=min(arr)
    aMax=max(arr)
    cMin=0
    cMax=0
    couMin=0
    couMax=0
    for i in arr:
        if(aMax == aMin and couMin<4 and couMax<4):
            cMin += i
            couMin += 1
            cMax += i
            couMax += 1
        if(i<aMax and couMin<4):
            cMin += i
            couMin += 1
        if(i>aMin and couMax<4):
            cMax += i
            couMax += 1
            
    print(cMin,cMax)  

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
