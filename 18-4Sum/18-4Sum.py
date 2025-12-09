# Last updated: 9.12.2025, 23:09:12
1class Solution:
2    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
3        nums.sort()
4        res = []
5        n = len(nums)
6        
7
8        for i in range(n - 3): 
9            if i > 0 and nums[i] == nums[i-1]:
10                continue
11            
12
13            for j in range(i + 1, n - 2): 
14                if j > i + 1 and nums[j] == nums[j-1]:
15                    continue
16                
17                l, r = j + 1, n - 1
18                while l < r:
19                    suma = nums[i] + nums[j] + nums[l] + nums[r]
20                    
21                    if suma < target:
22                        l += 1 
23                    elif suma > target:
24                        r -= 1 
25                    else:
26                        res.append([nums[i], nums[j], nums[l], nums[r]])
27                        
28                        l += 1
29                        r -= 1
30                        while l < r and nums[l] == nums[l-1]:
31                            l += 1
32                        while l < r and nums[r] == nums[r+1]:
33                            r -= 1
34                            
35        return res
36