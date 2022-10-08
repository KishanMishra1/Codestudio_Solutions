from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        sum3=sum(nums[:3])
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            while(left<right):
                sumx=nums[i]+nums[left]+nums[right]
                if sumx>target:
                    right-=1
                elif sumx<target:
                    left+=1
                else:
                    return sumx
                if abs(sumx-target)<abs(sum3-target):
                    sum3=sumx
        return sum3
