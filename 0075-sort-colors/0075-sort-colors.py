class Solution:
    def sortColors(self, nums: List[int]) -> None:

        for i in range(len(nums)):
            swapp=False

            for j in range(len(nums)-1-i):

                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
                    swapp=  True

            if not swapp:
                break
        return nums
        """
        Do not return anything, modify nums in-place instead.
        """
        