class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minnn=prices[0]
        max_profit=0
        for i in range(len(prices)):
            if prices[i]<minnn:
                minnn=prices[i]
            else:
                max_profit=max(max_profit,prices[i]-minnn)
        if max_profit>0:
            return max_profit
        else:
            return 0
                    

        
        
        