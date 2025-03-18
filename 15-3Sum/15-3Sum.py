class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def two_sum(nums, target, i):
            l, r = i + 1, len(nums) - 1
            result = []
            while l < r:
                total = nums[l] + nums[r]
                if total == target:
                    result.append([nums[i], nums[l], nums[r]])
                    # Skip duplicates for `l` and `r`
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    r -= 1
            return result
        
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates for `i`
                continue
            target = -nums[i]
            res.extend(two_sum(nums, target, i))
        
        return res



        