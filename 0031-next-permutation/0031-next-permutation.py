class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # Finding Pivot
        ptr1 = len(nums) - 1
        while ptr1 > 0 and nums[ptr1 - 1] >= nums[ptr1]:
            ptr1 -= 1
        
        # Edge case 
        if ptr1 == 0:
            nums.reverse()
            return

        pivot = ptr1 - 1

        # Finding smallest number greater than pivot
        ptr = len(nums) - 1
        while nums[ptr] <= nums[pivot]:
            ptr -= 1

  
        nums[pivot], nums[ptr] = nums[ptr], nums[pivot]

        # Reverse everything after the pivot.
        left = pivot + 1
        right = len(nums) - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1