from typing import List

def subsetSum(num: List[int]) -> List[int]:
    # Write your code here.
    n=len(num)
    final=[]
    ind=0
    sumx=0
    def subsets(ind,sumx,n,arr,res):
        if ind==n:
            res.append(sumx)
            return
        subsets(ind+1,sumx+arr[ind],n,arr,res)
        subsets(ind+1,sumx,n,arr,res)
    subsets(ind,sumx,n,num,final)
    return sorted(final)
