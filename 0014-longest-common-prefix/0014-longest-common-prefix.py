class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""

        stng = ""

        for i in range(len(strs[0])):
            char = strs[0][i]

            for words in strs:
                if i>=len(words) or words[i]!=char:
                    return stng
            stng+=char 

        return stng 
        

        