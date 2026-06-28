class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        reversed_num = 0
        x_=x
        while x_ > 0:
            digit = x_ % 10
            reversed_num = (reversed_num * 10) + digit
            x_ //= 10  
        if reversed_num==x:
            return True
        else:
            return False