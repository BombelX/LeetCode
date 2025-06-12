# Last updated: 12.06.2025, 09:37:37

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        p = [0] * n
        p[0] = nums[0]
        p[1] = max(nums[0], nums[1])
        for i in range(2, n):
            p[i] = max(p[i-1], p[i-2] + nums[i])
        return p[-1]
