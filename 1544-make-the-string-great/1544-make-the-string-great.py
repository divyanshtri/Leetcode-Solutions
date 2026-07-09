class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        for i in s:
            if stack:
                if stack[-1]==i.upper() and i.islower():
                    stack.pop()
                elif stack[-1]==i.lower() and i.isupper():
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        if stack==[]:
            return ""
        else:
            return ("".join(stack))

   