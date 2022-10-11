class Solution:
    def getRow(self, A: int) -> List[int]:
        def binomexpan(n,r):
            if r>n-r:
                r=n-r
            res=1
            for i in range(r):
                res*=(n-i)
                res//=(i+1)
            return res
        result=[]
        for i in range(A+1):
            result.append(binomexpan(A,i))
        return result
        
