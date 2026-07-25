class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        stng=""
        for i in s:
            freq[i]=freq.get(i,0)+1
        for j in range(len(freq)):
            max_key=max(freq,key=freq.get)
            temp=freq[max_key]
            while temp>0:
                stng+=max_key
                temp-=1
            freq.pop(max_key)
        return stng