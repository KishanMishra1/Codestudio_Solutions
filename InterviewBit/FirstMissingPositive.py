class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        positive={}
        pos=1
        for i in nums:
            if i>0:
                positive[i]=1
        while positive.get(pos,0):
            pos+=1
        return pos
