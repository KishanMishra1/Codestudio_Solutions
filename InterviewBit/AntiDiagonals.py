class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        n=len(A)
        res=[0]*(2*n-1)
        for i in range(2*n-1):
            res[i]=[]
        for i in range(n):
            for j in range((n)):
                res[i+j].append(A[i][j])
        return res





obj=Solution()
A=[[1,2,3],[3,4,6],[7,8,9]]
print(obj.diagonal(A))
