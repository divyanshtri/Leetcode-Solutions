class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict1={}
        seen=set()
        for i in arr:
            dict1[i]=dict1.get(i,0)+1
            seen.add(i)

        occr=set(dict1.values())
            
        return len(occr)==len(seen)