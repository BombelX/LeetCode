# Last updated: 21.05.2025, 18:17:22
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_buy = prices[0]
        best_profit = 0
        for price in prices[1:]:
            best_buy = min(price,best_buy)
            best_profit = max(best_profit,price-best_buy)
        return best_profit