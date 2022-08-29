from os import *
from sys import *
from collections import *
from math import *

def ninjaAndSortedArrays(arr1,arr2,m,n):
    # Write your code here.
    while(m>0 and n>0):
        if arr1[m-1]>arr2[n-1]:
            arr1[m+n-1]=arr1[m-1]
            m-=1
        else:
            arr1[m+n-1]=arr2[n-1]
            n-=1
    while(n>0):
        arr1[n-1]=arr2[n-1]
        n-=1
    return arr1
