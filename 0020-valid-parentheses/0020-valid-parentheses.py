class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        s1=set(["(","[","{"])
        s2=set([")","]","}"])
        pairs={
            ")":"(",
            "}":"{",
            "]":"["
        }
        for i in s:
            if i in s1:
                stk.append(i)
            elif i in s2:
                if stk and stk[-1] == pairs[i]:
                    stk.pop()
                else:
                    return False
        if not stk:
            return True
        else:
            return False
        