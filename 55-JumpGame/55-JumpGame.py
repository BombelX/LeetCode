# Last updated: 5.01.2026, 17:57:40
1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3        max_reach = 0
4        for i,jump in enumerate(nums):
5            if max_reach<i :
6                return False
7            else:
8                max_reach = max(max_reach,i+jump)
9        return True
10        