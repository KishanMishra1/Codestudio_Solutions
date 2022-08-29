from os import *
from sys import *
from collections import *
from math import *

def missingAndRepeating(arr, n):
    # Write your code here
    mis,dup=0,0
    countarr=[0]*(n+1)
    for i in range(n):
        countarr[arr[i]]+=1
    for i in range(1,n):
        if countarr[i]==0:
            mis=i
        elif countarr[i]>1:
            dup=i
    return [mis,dup]
        
