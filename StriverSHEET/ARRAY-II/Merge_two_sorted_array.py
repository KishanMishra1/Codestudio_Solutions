from os import *
from sys import *
from collections import *
from math import *

def ninjaAndSortedArrays(arr1,arr2,m,n):
    # Write your code here.
    arr1[m:]=arr2
    arr1.sort()
    return arr1
