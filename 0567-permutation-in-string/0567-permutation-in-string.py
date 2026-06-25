class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1=[0]*26
        win_count=[0]*26
        left=0

        for i in s1:
            index_to_add=ord(i)-ord('a')
            count1[index_to_add]+=1
            
            
        for right in range(len(s2)):  
            index_to_add2=ord(s2[right])-ord('a')
            win_count[index_to_add2]+=1
            win_size=right-left +1
            if win_size>len(s1):
                index_to_rm=ord(s2[left])-ord('a')
                win_count[index_to_rm]-=1
                left+=1
            if count1==win_count:
                return True
        return False
        