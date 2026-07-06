class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ptr1=0
        ptr2=0
        s.sort()
        g.sort()
        count=0
        while ptr1 <= len(g)-1 and ptr2 <= len(s)-1:
            if s[ptr2] >= g[ptr1]:
                count+=1
                ptr1+=1
                ptr2+=1
            else:
                ptr2+=1
        return count


        