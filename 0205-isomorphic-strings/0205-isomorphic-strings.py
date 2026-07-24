class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapp={}
        for j in range(len(s)):
            mapp[s[j]]=t[j]
        for i in range(len(s)):
            if mapp.get(s[i])==t[i]:
                continue
            else:
                return False
        if len(set(mapp.values()))==len(mapp.values()):
            return True
        else:
            return False
        
        