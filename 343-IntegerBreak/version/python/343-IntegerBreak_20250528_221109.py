# Last updated: 28.05.2025, 22:11:09
# :)
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {}
        def break_num(num):
            if num <= 1:
                return 1
            mid = num//2+num%2
            max_b = 1
            for i in range(1,mid+1):
                if num-i in dp:
                    x = max(dp[num-i],num-i)
                else:
                    x = max(break_num(num-i),num-i)
                max_b = max(max_b,x*i)
            dp[num] = max_b
            return max_b
        return break_num(n)