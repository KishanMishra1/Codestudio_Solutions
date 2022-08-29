from os import *
from sys import *
from collections import *
from math import *

def findDuplicate(arr:list, n:int):
    slow=arr[0]
    fast=arr[0]
    while True:
        slow=arr[slow]
        fast=arr[arr[fast]]
        if slow==fast:
            break
    ptr1=arr[0]
    ptr2=fast
    while(ptr1!=ptr2):
        ptr1=arr[ptr1]
        ptr2=arr[ptr2]
    return int(ptr1)
