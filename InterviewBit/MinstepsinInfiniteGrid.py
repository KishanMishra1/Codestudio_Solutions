class Solution:

    # @param A : integer
    # @return a strings
    def solve(self,A,B):
        x=A[0]
        y=B[0]
        total=0
        for i,j in zip(A,B):
            dx,dy=abs(i-x),abs(j-y)
            if dx>dy:
                total+=dx
            else:
                total+=dy
            x,y=i,j
        return total





obj=Solution()
A = [0, 1, 1]
B = [0, 1, 2]
print(obj.solve(A,B))
