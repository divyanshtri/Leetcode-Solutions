class Solution:
    def isPalindrome(self, x: int) -> bool:
        stng=str(x)
        rev=stng[::-1]
        if rev==stng:
            return True
        else:
            return False