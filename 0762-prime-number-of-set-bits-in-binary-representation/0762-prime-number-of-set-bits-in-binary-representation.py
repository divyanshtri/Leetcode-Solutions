class Solution:
    def is_prime(self,n):
        if n <=1:
            return False
        for i in range(2,n):
            if n%i==0:
                return False
        return True
    def countPrimeSetBits(self, left: int, right: int) -> int:
        countp=0
        for i in range(left,right+1):
            ib=bin(i)[2:]
            count=0
            for j in (ib):
                if j == "1":
                    count+=1
            if self.is_prime(count)==True:
                countp+=1
        return countp



        