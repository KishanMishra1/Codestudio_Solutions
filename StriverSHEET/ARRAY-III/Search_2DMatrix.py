from os import *
from sys import *
from collections import *
from math import *

def findTargetInMatrix(mat, m, n, target):
	# Write your code here.
    left=0
    right=(m*n)-1
    while(left<=right):
        
        mid=(left+(right-left)//2)
        if mat[mid//n][mid%n]==target:
            return True
        elif mat[mid//n][mid%n]>target:
            right=mid-1
        else:
            left=mid+1
    return False
