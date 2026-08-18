class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low=1
        high = max(nums)

        def findsum(div):
            summ=0
            for num in nums:
                summ += (num + div - 1) // div
            return summ

        while low < high:
            mid= low + (high-low)//2

            if findsum(mid)<=threshold:
                high=mid 
            else:
                low=mid+1
                
        return low




        