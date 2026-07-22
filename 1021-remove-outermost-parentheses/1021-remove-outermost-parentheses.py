class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depth = 0
        ans=[]
        for i in s:
            if i=="(":
                depth+=1
                if depth >1:
                    ans.append(i)
            else:
                depth-=1
                if depth>=1:
                    ans.append(i)
        res="".join(ans)
        return res

