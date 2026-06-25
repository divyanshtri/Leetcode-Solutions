class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn=prices[0]
        max_profit=0
        for i in range(len(prices)):
            if prices[i]<minn:
                minn=prices[i]
            else:
                max_profit=max(max_profit,prices[i]-minn)
        if max_profit>0:
            return max_profit
        else:
            return 0
                    

        
        
        