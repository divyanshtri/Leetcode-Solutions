class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        while k>0:
            nums.insert(0,nums.pop())
            k-=1
        return nums
        """
        Do not return anything, modify nums in-place instead.
        """
        