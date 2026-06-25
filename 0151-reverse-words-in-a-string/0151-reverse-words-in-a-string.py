class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        s=" ".join(s.split())
        arr=s.split()
        arr.reverse()
        s=" ".join(arr)
        return s
        