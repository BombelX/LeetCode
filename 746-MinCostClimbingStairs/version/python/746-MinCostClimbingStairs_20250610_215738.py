# Last updated: 10.06.2025, 21:57:38
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n<2:
            return 0
        elif n == 2:
            return min(cost[0],cost[1])


        dp = [0]*len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,len(cost)):
            dp[i] = cost[i] + min(dp[i-1],dp[i-2])
        return min(dp[-1],dp[-2])