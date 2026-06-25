class Solution:
    def containsDuplicate(self,nums: List[int]) -> bool:
        lst=set()
        for i in range(len(nums)):
            if nums[i] not in lst:
                lst.add(nums[i])
        if len(lst)!=len(nums):
            return True
        else:
            return False

        