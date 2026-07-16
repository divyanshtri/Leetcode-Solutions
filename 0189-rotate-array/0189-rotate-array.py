class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        m = len(nums)
        k %= m

       
        nums.reverse()

        
        left, right = 0, k - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        
        left, right = k, m - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        """
        Do not return anything, modify nums in-place instead.
        """
        