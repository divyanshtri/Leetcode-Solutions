class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ans = [0] * len(code)
        n=len(code)
        for i in range(len(code)):
            if k>0:
                summ=0
                for j in range(1,k+1):
                    summ+=code[(i+j)%n] #moving fwd
                ans[i]=summ

            elif k<0:
                sum_=0
                for l in range(1,abs(k)+1):
                    sum_+=code[(i-l)%n] #moving bkwd
                ans[i]=sum_
            else:
                return ans
        return ans
            
            



        