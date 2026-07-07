class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start_pts=set()
        end_pts=set()
        for j in paths:
            start_pts.add(j[0])
            end_pts.add(j[1])
        s=end_pts-start_pts.intersection(end_pts)
        for a in s:
            return a
        
        
        
        