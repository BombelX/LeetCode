# Last updated: 28.05.2025, 19:20:27
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_buy = prices[0]
        best_profit = 0
        for price in prices[1:]:
            best_buy = min(price,best_buy)
            best_profit = max(best_profit,price-best_buy)
        return best_profit