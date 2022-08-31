from os import *
from sys import *
from collections import *
from math import *

import sys
sys.setrecursionlimit(10**7)

def modularExponentiation(x, n, m):
    if x==0:
        return 0
    if n==0:
        return 1
    temp=n
    ans=1
    if n<0:
        temp=(-1)*n
    while(temp>0):
        if temp%2==0:
            x=x*x
            temp//=2
        else:
            ans*=x
            temp-=1
    if n<0:
        return (1/(ans))%m
    else:
        return ans%m
# Main.
t = int(input())
while (t > 0):
    lst = list(map(int,input().split()))
    x,n,m = lst[0], lst[1], lst[2]
    print(modularExponentiation(x, n, m))
    t -= 1
