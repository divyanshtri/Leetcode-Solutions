class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        for i in range (numRows):
            if i == 0:
                ans.append([1])
            elif i==1:
                ans.append([1,1])
            else:
                arr=[]
                for j in range (i+1):
                    if j==0:
                        arr.append(1)
                    elif j==i:
                        arr.append(1)
                    else:
                        val=ans[-1][j-1] + ans[-1][j]
                        arr.append(val)
                ans.append(arr)
        return ans