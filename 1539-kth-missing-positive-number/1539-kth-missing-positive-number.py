class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        low = 0
        highh = len(arr) - 1

        while low <= highh:

            mid = low + (highh - low) // 2

            
            missing = arr[mid] - (mid + 1)

            if missing < k:
                low = mid + 1

            else:
                highh = mid - 1

        return low + k