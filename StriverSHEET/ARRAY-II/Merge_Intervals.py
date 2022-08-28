from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit


def mergeIntervals(intervals):
    stack = []
    intervals.sort()
    for s, e in intervals:
        if stack and stack[-1][1] >= s:
            stack[-1] = [stack[-1][0], max(stack[-1][1], e)]
        else:
            stack.append([s, e])
    return stack


n = int(input())
arr1 = list(map(int, stdin.readline().strip().split(" ")))
arr2 = list(map(int, stdin.readline().strip().split(" ")))
intervals=[]
for i in zip(arr1,arr2):
    intervals.append([*i])
res=mergeIntervals(intervals)
for i in res:
    print(*i)
