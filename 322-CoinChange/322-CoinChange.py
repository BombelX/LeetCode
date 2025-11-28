# Last updated: 28.11.2025, 19:20:58
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def coin_v(amount,coins):
            if amount == 0:
                return 1
            elif amount<0:
                return float('inf')
            nonlocal dp
            min_coins = float('inf')
            for coin in coins:
                if coin>amount:
                    break
                if amount-coin in dp:
                    min_coins = min(min_coins,dp[amount-coin])
                else:
                    x = coin_v(amount-coin,coins)
                    min_coins = min(min_coins,x)
            dp[amount] = min_coins+1
            return min_coins+1
        x = coin_v(amount,sorted(coins))
        if x == float('inf'):
            return -1
        else:
            return x-1
