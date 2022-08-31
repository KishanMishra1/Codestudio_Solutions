from os import *
from sys import *
from collections import *
import math

import sys
sys.setrecursionlimit(10**7)

def modularExponentiation(x, n, m):
    return pow(x,n,m)
# Main.
t = int(input())
while (t > 0):
    lst = list(map(int,input().split()))
    x,n,m = lst[0], lst[1], lst[2]
    print(modularExponentiation(x, n, m))
    t -= 1
