class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math 
        low = 1
        high = max(piles)

        while low <= high:

            k = low + (high - low) // 2

            time = 0

            for pile in piles:
                a=math.ceil(pile/k)
                time += a

            if time <= h:
                high=k-1

            else:
                low=k+1

        return low