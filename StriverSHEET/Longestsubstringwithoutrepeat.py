#User function Template for python3

class Solution:
    def longestUniqueSubsttr(self, S):
        # code here
        res=[]
        maxlen=0
        for i in S:
            while i in res:
                res.pop(0)
            if i not in res:
                res.append(i)
                maxlen=max(maxlen,len(res))
        return maxlen


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        s = input().strip()
        
        
        ob=Solution()
        print(ob.longestUniqueSubsttr(s))
# } Driver Code Ends
