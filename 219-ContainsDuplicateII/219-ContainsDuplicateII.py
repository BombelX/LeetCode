# Last updated: 5.01.2026, 18:40:13
1class Solution:
2    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
3        meeted = {}
4        
5        for index,num in enumerate(nums):
6            
7            if num in meeted:
8                for i in meeted[num]:
9                    if abs(index-i) <= k:
10                        return True
11
12                meeted[num].append(index)
13            else:
14                meeted[num] = [index]
15        return False 
16
17
18
19        