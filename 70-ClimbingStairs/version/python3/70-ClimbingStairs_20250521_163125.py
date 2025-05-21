# Last updated: 21.05.2025, 16:31:25
class Solution:
    def climbStairs(self, n: int) -> int:
        stairs = [0]*(n+1)
        stairs[0] = 1
        for i in range(n+1):
            if i+1<=n:
                stairs[i+1]+=stairs[i]
            if i+2<=n:
                stairs[i+2]+=stairs[i]
        return stairs[n]
