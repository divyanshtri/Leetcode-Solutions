class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        low = max(weights)
        high = sum(weights)

        def capacity(cap):

            current_weight = 0
            required_dayss = 1

            for weight in weights:

                if current_weight + weight <= cap:
                    current_weight += weight

                else:
                    required_dayss += 1
                    current_weight = weight

            return required_dayss <= days

        while low < high:

            mid = low + (high - low) // 2

            if capacity(mid):
                high = mid

            else:
                low = mid + 1

        return low