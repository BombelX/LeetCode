# Last updated: 28.11.2025, 19:21:01
# class Solution:
#     def maxCoins(self, nums: List[int]) -> int:
#         ln = len(nums)
#         if ln == 0:
#             return 0
#         if ln == 1:
#             return nums[0]
#         dp = {}
#         n = len(nums)
#         def burst(tb,n):
#             if tuple(tb) in dp:
#                 return dp[tuple(tb)]
#             sm = 0
#             if n>3:
#                 for i in range(1,n-1):
#                     tmp = tb[:]
#                     tmp.pop(i)
#                     sm = max(sm,burst(tmp,n-1)+tb[i-1]*tb[i]*tb[i+1])
#                 tmp = tb[:]
#                 tmp.pop(0)
#                 sm = max(sm,burst(tmp,n-1)+tb[0]*tb[1])
#                 tmp = tb[:]
#                 tmp.pop(-1)
#                 sm = max(sm,burst(tmp,n-1)+tb[-2]*tb[-1])
                
#             if n==3:
#                 tmp = tb[:]
#                 tmp.pop(1)
#                 sm = max(sm,burst(tmp,n-1)+tb[0]*tb[1]*tb[2])
#             if n==2:
#                 sm = min(tb)*max(tb) + (max(tb))
#             dp.update({tuple(tb):sm})
#             return sm
#         return burst(nums,n)
                
                    
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        for gap in range(2, n):        
            for l in range(0, n - gap):
                r = l + gap
                for i in range(l+1, r):
                    coins = nums[l] * nums[i] * nums[r]
                    total = dp[l][i] + coins + dp[i][r]
                    if total > dp[l][r]:
                        dp[l][r] = total
        return dp[0][n-1]
