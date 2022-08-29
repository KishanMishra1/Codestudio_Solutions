from os import *
from sys import *
from collections import *
from math import *

def missingAndRepeating(a, n):
    # Write your code here
    ts=(len(a)*(len(a)+1))//2
    d=[0]*len(a)
    for i in a:
        if d[i-1]==1:
            return [ts-(sum(a)-i),i]
        else:
            d[i-1]=1
        
