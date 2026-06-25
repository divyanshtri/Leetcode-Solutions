class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        max_freq=0
        count={}
        ans=0

        for right in range (len(s)):
            count[s[right]]=count.get(s[right],0)+1
            max_freq = max(max_freq, count[s[right]])
            win_size=right-left+1
            replacement= win_size-max_freq
            
            while(replacement>k):
                count[s[left]] -= 1
                left+=1
                win_size=right-left+1
                replacement= win_size-max_freq
            ans=max(ans,win_size)
        return ans
                