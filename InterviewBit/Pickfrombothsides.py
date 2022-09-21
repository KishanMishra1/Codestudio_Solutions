class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        S = sum(A[:B])
        m = S
        for k in range(1,B+1):
            S = S - A[B-k] + A[-k]
            m = max(m, S)
        return m
