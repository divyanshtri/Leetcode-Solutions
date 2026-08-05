class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        
        sign = 1
        index = 0
        
        
        if s[0] == '-':
            sign = -1
            index += 1
        elif s[0] == '+':
            index += 1
            
        
        res = 0
        while index < len(s) and s[index].isdigit():
            res = res * 10 + int(s[index])
            index += 1
            
        
        res *= sign
    

        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
            
        return res
