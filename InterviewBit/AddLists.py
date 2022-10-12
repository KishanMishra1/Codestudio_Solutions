class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def addArrays(self, A, B):

        carry=0
        sumarr=[]
        i=len(A)-1
        j=len(B)-1
        while(i>=0 and j>=0):
            sumx=(A[i]+B[j]+carry)

            sumarr.append(sumx%10)
            carry = sumx // 10
            i -= 1
            j -= 1

        while (i >= 0):
            sumx = (A[i]+ carry)

            sumarr.append(sumx % 10)
            carry = sumx // 10
            i -= 1

        while (j >= 0):
            sumx = (B[j] + carry)
            sumarr.append(sumx % 10)
            carry = sumx // 10
            j -= 1

        if carry>0:
            sumarr.append(carry)
            i-=1
            j-=1
        return sumarr[::-1]

obj=Solution()
A = [ 4, 3, 6, 7, 9, 9, 1, 7, 8 ]
B = [ 7, 5, 8, 9 ]

print(obj.addArrays(A,B))
