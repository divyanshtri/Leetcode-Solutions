class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count1={}
        count2={}

        for i in ransomNote:
            count1[i]=count1.get(i,0)+1
        for j in magazine:
            count2[j]=count2.get(j,0)+1
        for ch in count1:
            if count1[ch] > count2.get(ch, 0):
                return False
        return True 