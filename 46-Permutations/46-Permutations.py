# Last updated: 23.04.2026, 14:48:56
1class Solution:
2    def permute(self, nums: List[int]) -> List[List[int]]:
3        res = []
4        used = [False] * len(nums)
5        def perm(curr):
6            if len(curr) == len(nums):
7                res.append(curr[:])
8                return
9            for i in range(len(nums)):
10                if not used[i]:
11                    used[i] = True
12                    curr.append(nums[i])
13                    perm(curr)
14                    curr.pop()
15                    used[i] = False
16        perm([])
17        return res
18
19
20        