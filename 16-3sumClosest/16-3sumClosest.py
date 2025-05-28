# Last updated: 28.05.2025, 19:20:54
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  
        closest = float('inf') 
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]: 
                continue
            l, r = i + 1, len(nums) - 1  
            while l < r:
                total = nums[i] + nums[l] + nums[r]  
                if abs(total - target) < abs(closest - target):
                    closest = total

                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    return total
        return closest  

