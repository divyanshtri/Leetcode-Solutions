class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        ans=0
        for i in range(len(nums)):
            if i==len(nums)-1 and nums[i]==1:
                count+=1
                ans=max(ans,count)
                count=0
            elif nums[i]==1:
                count+=1
            else:
                ans=max(ans,count)
                count=0
        return ans

        