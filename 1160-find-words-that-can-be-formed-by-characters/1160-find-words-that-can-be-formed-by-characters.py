class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq_c={}
        answer=0 

        for i in chars:
            freq_c[i]=freq_c.get(i,0)+1

        
        for i in range(len(words)):
            freq_w={}
            for j in words[i]:
                freq_w[j]=freq_w.get(j,0)+1

            valid= True
            for ch in freq_w:
                if freq_c.get(ch, 0)<freq_w[ch]:
                    valid= False
                    break

            if valid:
                answer += len(words[i])

        return answer


        