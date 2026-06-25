class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num=str(num)

        left=0
        right=k-1
        count=0
        for i in range(len(num) - k + 1):
            substring = int(num[i:i+k])
            if substring!=0 and int(num)%substring==0:
                count+=1
                left+=1
                right+=1
        return count 
                