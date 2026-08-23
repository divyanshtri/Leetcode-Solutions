class Solution:
    def maxDepth(self, s: str) -> int:
        left = []
        right= []

        max_depth=0
        
        for char in s:
            if  char=="(":
                left.append(char)
            if char == ")":
                right.append(char)

            depth = len(left) - len(right)

            max_depth=max(max_depth,depth)
        
        return max_depth 
