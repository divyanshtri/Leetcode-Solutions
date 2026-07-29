class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        nums = sorted(set(nums))

        ans = 1
        left = 0

        for right in range(len(nums)):

            if right != len(nums)-1 and nums[right+1] == nums[right] + 1:
                continue

            ans = max(ans, right - left + 1)
            left = right + 1

        return ans