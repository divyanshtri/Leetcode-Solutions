class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sett=set()
        sett2=set()
        for i in nums1:
            sett.add(i)
        for j in nums2:
            sett2.add(j)
        return (list(sett & sett2))