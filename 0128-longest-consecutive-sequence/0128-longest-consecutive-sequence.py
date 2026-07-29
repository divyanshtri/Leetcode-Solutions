class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans=0
        num=set(nums)
        num1=list(num)
        num1.sort()
        left=0
        for right in range(len(num1)):
            if right!=len(num1)-1 and num1[right+1]==num1[right]+1:
                right+=1
            else:
                ans=max(ans,len(num1[left:right+1]))
                right+=1
                left=right
            
        return ans
        