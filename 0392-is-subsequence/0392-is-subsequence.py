class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_ptr = 0

        for char in t:
            if s_ptr < len(s) and s[s_ptr] == char:
                s_ptr += 1

        return s_ptr == len(s)
