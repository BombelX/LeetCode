# Last updated: 28.11.2025, 17:39:12
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        min_meeted = float('inf')
4        max_delta = float('-inf')
5        for price in prices:
6            max_delta = max(max_delta,price-min_meeted)
7            min_meeted = min(min_meeted,price)
8        if max_delta>0:
9            return max_delta
10        return 0