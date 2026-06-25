class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum=[]
        sum_l=0
        for i in range (len(nums)):
            if i==0:
                left_sum.append(0)
                sum_l+=nums[i]
            else:
                left_sum.append(sum_l)   
                sum_l+=nums[i]          
        right_sum=[]
        sum_r=0
        for i in range (len(nums)-1,-1,-1):      
            if i==len(nums)-1:
                right_sum.append(0)
                sum_r+=nums[i]
            else:
                right_sum.append(sum_r)
                sum_r+=nums[i]
        right_sum.reverse()
        for i in range(len(left_sum)):
            if left_sum[i]==right_sum[i]:
                return(i)
                break
        return -1
