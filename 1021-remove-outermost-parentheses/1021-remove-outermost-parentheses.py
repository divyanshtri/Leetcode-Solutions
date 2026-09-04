class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depth = 0
        answer=[]
        for i in s:
            if i=="(":
                depth+=1
                if depth >1:
                    answer.append(i)
            else:
                depth-=1
                if depth>=1:
                    answer.append(i)
        result="".join(answer)
        return result
        

