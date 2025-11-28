# Last updated: 28.11.2025, 19:20:51
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        dp = {}
        n = len(nums)
        def go(l, r, p, p1, p2):
            if l == r:
                if p == 0:
                    return (p1 + nums[l]) >= p2
                else:
                    return p1 >= (p2 + nums[l])
            
            key = (l, r, p, p1, p2)
            if key in dp:
                return dp[key]

            if p == 0:
                take_l = go(l+1, r, 1, p1+nums[l], p2)
                take_r = go(l, r-1, 1, p1+nums[r], p2)
                res = take_l or take_r
            else:
                take_l = go(l+1, r, 0, p1, p2+nums[l])
                take_r = go(l, r-1, 0, p1, p2+nums[r])
                res = take_l and take_r

            dp[key] = res
            return res

        return go(0, n-1, 0, 0, 0)
