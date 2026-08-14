class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        countt = 0

        freq = {0: 1}

        for num in nums:
            prefix += num

            needed = prefix - k

            if needed in freq:
                countt += freq[needed]

            freq[prefix] = freq.get(prefix, 0) + 1       
        
        return countt