
class Solution:
    # @param A : tuple of integers
    # @return a strings
    def solve(self,A):
        res=[]
        while A:
            if abs(A[0])>abs(A[-1]):
                k=A.pop(0)
            else:
                k=A.pop(-1)
            res.append(k*k)
        return res[::-1]
