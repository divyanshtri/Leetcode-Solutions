class Solution:
    def findGCD(self, nums: List[int]) -> int:
            minn=min(nums)
            maxx=max(nums)
            while minn != 0:
                maxx , minn = minn , maxx % minn
            return maxx