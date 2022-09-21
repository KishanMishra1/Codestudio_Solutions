class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        max_tl=0
        max_sum=0
        s=0
        start=0
        end=0
        allnegs=0
        if len(A)==0:
            return []
        if sum(A)==(-1)*(len(A)):
            return []
        for i in range(len(A)):
            if A[i]>0:
                max_tl+=A[i]
            else:
                s=i+1
                max_tl=0
            if max_tl>max_sum:
                max_sum=max_tl
                start=s
                end=i
        if max_sum>=0:
            return A[start:end+1]
