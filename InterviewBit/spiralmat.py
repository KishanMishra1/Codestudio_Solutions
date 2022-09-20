class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        res=[]
        left,right=0,len(A[0])-1
        top,bottom=0,len(A)-1
        k=0

        while(left<=right and top<=bottom):
            if k==0:
                for i in range(left,right+1):
                    res.append(A[top][i])
                top+=1
            if k==1:
                for i in range(top,bottom+1):
                    res.append(A[i][right])
                right-=1
            if k==2:
                for i in range(right,left-1,-1):
                    res.append(A[bottom][i])
                bottom-=1
            if k==3:
                for i in range(bottom,top-1,-1):
                    res.append(A[i][left])
                left+=1
            k=(k+1)%4
        return res



obj=Solution()
arr=[
    [ 1, 2, 3,4 ],
    [ 4, 5, 6,9 ],
    [ 7, 8, 9 ,12]
]
print(obj.spiralOrder(arr))
