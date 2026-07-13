class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result=[]
        for i in range(len(prices)):
            j=i+1
            discount=0
            while(j > i and j < len(prices)):
                if prices[j]<=prices[i]:
                    discount=prices[j]
                    break
                j+=1
            result.append(prices[i]-discount)
        return result