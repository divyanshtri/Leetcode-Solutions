class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0:
            return 0
        t=str(n)
        sum=0
        arr=[]

        for i in t:
            if i!="0":
                arr.append(i)
        x=int("".join(arr))
        for j in arr:
            sum+=int(j)
        return x*sum

        