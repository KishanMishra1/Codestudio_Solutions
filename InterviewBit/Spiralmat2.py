class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of list of integers
    def solve(self, A, B, C):
        mat=[]
        for i in range(B):
            mat.append([0]*C)
        pointer=0
        left,right=0,C-1
        top,down=0,B-1
        dir=0
        while left<=right and top<=down:
            if dir==0:
                for i in range(left,right+1):
                    mat[top][i]=A[pointer]
                    pointer+=1
                top+=1
            elif dir==1:
                for i in range(top,down+1):
                    mat[i][right]=A[pointer]
                    pointer+=1
                right-=1
            elif dir==2:
                for i in range(right,left-1,-1):
                    mat[down][i]=A[pointer]
                    pointer+=1
                down-=1
            elif dir==3:
                for i in range(down,top-1,-1):
                    mat[i][left]=A[pointer]
                    pointer+=1
                left+=1
            dir=(dir+1)%4
        return mat        
        
