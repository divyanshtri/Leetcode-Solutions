class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stk=[]
        t_stk=[]

        for char in s:
            if char !="#":
                s_stk.append(char)
            elif char=="#" and not s_stk:
                continue
            else:
                s_stk.pop()        
        for char in t:
            if char !="#":
                t_stk.append(char)
            elif char=="#" and not t_stk:
                continue
            else:
                t_stk.pop()        

        return (s_stk==t_stk)
                