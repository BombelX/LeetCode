# Last updated: 28.11.2025, 19:21:18
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = {}
        def jmp(i):
            if i in dp:
                return dp[i]
            if i >= len(nums)-1:
                return 0

            dp_val = float('inf')

            for x in range(i+1,i+nums[i]+1):
                dp_val = min(dp_val,jmp(x)) 
            
            dp.update({i:dp_val+1})
            return dp_val+1
        return jmp(0)
