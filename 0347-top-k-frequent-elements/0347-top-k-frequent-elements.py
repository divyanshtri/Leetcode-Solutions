class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        answer=[]
        for i in nums:
            freq[i]=freq.get(i,0)+1

        pairs=list(freq.items())

        arr=sorted(pairs, key=lambda x: x[1], reverse=True)

        for j in range(k):
            answer.append(arr[j][0])

        return answer

            

            
        