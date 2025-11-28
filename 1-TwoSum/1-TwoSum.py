# Last updated: 28.11.2025, 17:28:02
1class Solution:
2
3    def twoSum(self, nums: List[int], target: int) -> List[int]:
4
5        visited = {}
6
7        for index,num in enumerate(nums):
8
9            if target-num in visited.keys():
10
11                return [index,visited[target-num]]
12
13            visited[num] = index