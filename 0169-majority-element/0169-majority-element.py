class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1={}
        for i in range(len(nums)):
            if nums[i] not in dict1:
                dict1[nums[i]]=0
            else:
                dict1[nums[i]]+=1
        max_key = max(dict1,key=dict1.get)
        return max_key