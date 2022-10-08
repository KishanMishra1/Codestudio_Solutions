from functools import cmp_to_key

class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, nums):
        if not any(nums):
            return "0"
        nums=map(str, nums)
        #print(nums)
        key=cmp_to_key(lambda n1, n2: -1 if n1 + n2 > n2 + n1 else (1 if n1 + n2 < n2 + n1 else 0))
        return "".join(sorted(nums, key=key))
