class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seeen={}

        for i in range(len(nums)):
            complement=target-nums[i]

            if complement in seeen:
                return [i,seeen[complement]]
                
            seeen[nums[i]]=i


        




                
            

