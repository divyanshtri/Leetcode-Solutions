class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        max_areaa=0
        while(left<right):
            width=right-left
            area=width*(min(height[left],height[right]))
            max_areaa = max(max_areaa, area)
            if height[right]<height[left]:
                right-=1
            else:
                left+=1
        return (max_areaa)