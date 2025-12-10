# Last updated: 10.12.2025, 20:24:22
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -float('inf')
        lls = 0
        for num in nums:
            if lls+num>num:
                lls +=num
                max_sum = max(lls,max_sum)
            else:
                lls = num
                max_sum = max(lls,max_sum)
            
        return max_sum