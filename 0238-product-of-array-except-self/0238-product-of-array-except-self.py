class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product=1
        right_product=1
        result=[] 
        result_r=[]
        answer=[]
        for i in range(len(nums)):
            result.append(left_product)
            left_product *= nums[i]
        for i in range(len(nums)-1,-1,-1):
            result_r.append(right_product)    
            right_product *= nums[i]
        result_r.reverse()
        for i in range (len(result)):
            answer.append(result[i]*result_r[i])
        return answer
            
        




        