class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result=[]
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            x=nums[i]
            left=i+1
            right=len(nums)-1

            while left < right:
                
                if x+nums[left]+nums[right]==0:
                    result.append([x,nums[left],nums[right]])
                    left+=1
                    right-=1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif  x+nums[left]+nums[right]>0:
                    right-=1
                else:
                    left+=1
                    

        return result