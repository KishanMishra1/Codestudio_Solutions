# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        def getlist(head):
            arr=[]
            if head==None:
                print("LinkedList input is empty !")
            else:
                itr=head
                while itr:
                    arr.append(itr.val)
                    itr=itr.next
            return arr
        def spiral_matrix(A,m,n):
            mat=[]
            ptr=0
            cp=0
            for i in range(m * n - len(A)):
                A.append(-1)
            for i in range(m):
                mat.append([0]*n)
            left,right=0,n-1
            top,down=0,m-1

            while(left<=right and top<=down):
                if cp==0:
                    for i in range(left,right+1):
                        mat[top][i]=A[ptr]
                        ptr+=1
                    top+=1
                elif cp==1:
                    for i in range(top,down+1):
                        mat[i][right]=A[ptr]
                        ptr+=1
                    right-=1
                elif cp==2:
                    for i in range(right,left-1,-1):
                        mat[down][i]=A[ptr]
                        ptr+=1
                    down-=1
                elif cp==3:
                    for i in range(down,top-1,-1):
                        mat[i][left]=A[ptr]
                        ptr+=1
                    left+=1
                cp=(cp+1)%4

            return mat
        return spiral_matrix(getlist(head),m,n)
