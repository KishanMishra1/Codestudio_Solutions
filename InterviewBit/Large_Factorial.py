class Solution:
    # @param A : integer
    #@return a strings
    def solve1(self, n):
        #recursion
        if n==1:
            return n
        else:
            return n * self.solve(n - 1)
    def solve(self,n):
        #memoziation
        def fac(n,tmp):
            tmp[0]=1
            for i in range(1,n+1):
                tmp.append(i*tmp[i-1])
            return tmp[n]

        tmp=[n+1]
        return fac(n,tmp)
        
            
