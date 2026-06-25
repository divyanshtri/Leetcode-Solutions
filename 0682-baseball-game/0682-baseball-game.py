class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for record in operations:
            if record=="C":
                stack.pop()
            elif record=="D":
                stack.append(int(stack[-1])*2)
            elif record=="+":
                stack.append(int(stack[-1])+int(stack[-2]))
            else:
                    stack.append(record)
        sum=0
        for i in stack:
            if not stack:
                return 0
            else:
                sum+=int(i)
        return sum
        