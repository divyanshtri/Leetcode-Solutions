class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q1=deque()
        q2=deque()
        for i,char in enumerate(senate):
            if char == "R":
                q1.append(i)
            else:
                q2.append(i)
        while q1 and q2:
            r=q1.popleft()
            s=q2.popleft()
            if r<s:
                q1.append(r+len(senate))
            else:
                q2.append(s+len(senate))
        if q1:
            return "Radiant"
        else:
            return "Dire"