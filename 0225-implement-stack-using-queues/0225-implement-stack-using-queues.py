class MyStack:

    def __init__(self):
        self.instack=[]
        self.outstack=[]
        

    def push(self, x: int) -> None:
        if self.instack==[]:
            self.instack.append(x)
        else:
            self.outstack.insert(0,self.instack.pop())
            self.instack.append(x)


    def pop(self) -> int:
        if len(self.instack)>0:
            s=self.instack.pop(0)
            return s
        else:  
            t=self.outstack.pop(0)
            return t

    def top(self) -> int:
        if len(self.instack)>0:
            return self.instack[0]
        else:
            return self.outstack[0]

    def empty(self) -> bool:
        if self.instack==[] and self.outstack==[]:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()