# Last updated: 10.12.2025, 17:58:32
1
2class Solution:
3    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
4        stack = []
5        mapping = {} 
6
7        for num in nums2:
8            while stack and stack[-1] < num:
9                val = stack.pop()
10                mapping[val] = num
11            
12            stack.append(num)
13        res = []
14        for num in nums1:
15            res.append(mapping.get(num, -1))
16            
17        return res
18
19