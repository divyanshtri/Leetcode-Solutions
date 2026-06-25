class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nextt=0
        k=0
        for i in nums:
            if i != val:
                nums[nextt]=i
                nextt+=1
                k+=1
        return k


        