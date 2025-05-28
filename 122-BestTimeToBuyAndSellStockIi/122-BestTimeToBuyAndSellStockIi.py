# Last updated: 28.05.2025, 19:20:26
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        diffrences = [0]*len(prices)
        for i in range(1,n):
            diffrences[i] = prices[i]-prices[i-1]
        res = 0
        for diff in diffrences:
            if diff > 0:  
                res += diff
        return res