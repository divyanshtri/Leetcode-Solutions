def calculate_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd=0
        sumeven=0
        for i in range(1,(n*2)+1):
            if i%2==0:
                sumeven+=i
            else:
                sumOdd+=i
        a=calculate_gcd(sumOdd,sumeven)
        return a