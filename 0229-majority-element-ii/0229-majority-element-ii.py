class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        seen={}
        
        for i in nums:
            seen[i]=seen.get(i,0) + 1

        ans=[]
        
        for num , count in seen.items():
            if count > len(nums) / 3:
                ans.append(num)

        return ans