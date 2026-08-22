class Solution:
    def checkDivisibility(self, n: int) -> bool:
        n_str=str(n)
        int_sum=0
        product=1
        for num in n_str:
            int_sum+=int(num)
            product*=int(num) 

        summ = int_sum + product
        
        if (n%summ)==0:
            return True
        else:
            return False  