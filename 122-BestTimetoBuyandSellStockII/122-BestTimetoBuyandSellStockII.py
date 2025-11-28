# Last updated: 28.11.2025, 17:49:44
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        income = 0
4        possible_buy_price = prices[0]
5        for price in prices:
6            if price > possible_buy_price:
7                income += price-possible_buy_price
8            possible_buy_price = price
9        
10        return income