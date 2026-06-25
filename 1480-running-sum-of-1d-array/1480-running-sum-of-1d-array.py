class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum=[]
        summ=0
        for i in range(len(nums)):
            if i==0:
                running_sum.append(nums[0])
                summ+=nums[0]
            else:
                summ+=nums[i]
                running_sum.append(summ)
        return running_sum


