#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    posCount=0
    negCount=0
    zeroCount=0
    for i in arr:
        if(i>0):
            posCount+=1
        elif(i<0):
            negCount+=1
        else:
            zeroCount+=1
    print (posCount/n)
    print (negCount/n)
    print (zeroCount/n)
            
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
