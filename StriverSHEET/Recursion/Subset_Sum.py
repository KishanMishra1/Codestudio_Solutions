from typing import List

def subsetSum(num: List[int]) -> List[int]:
    # Write your code here.
    n=len(num)
    final=[]
    for i in range(int(1<<n)):
        res=[]
        for j in range(0,n):
            if i&(1<<j):
                res.append(num[j])
        final.append(sum(res)) #n*2^n
    return sorted(final) #nlogn
