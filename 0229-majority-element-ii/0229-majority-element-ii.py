class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        seen={}
        ans=set()
        for i in nums:
            seen[i]=seen.get(i,0) + 1

        length = len(nums)/3
        
        for num in nums:
            if seen[num]>length and num not in ans:
                ans.add(num)

        res=list(ans)
        return res