class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen={}
        strr=""
        for i in range(len(s)):
            seen[s[i]]=seen.get(s[i],0)+1
        for key in seen:
            if seen.get(key,0)==1:
                strr=key
                break
        if strr=="":
            return -1
        else:
            return s.find(strr)
