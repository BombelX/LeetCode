# Last updated: 22.08.2026, 19:29:36
1class Solution:
2    def summaryRanges(self, nums: List[int]) -> List[str]:
3
4        ranges = []
5        if len(nums) == 0:
6            return []
7
8        start = nums[0]
9        last_one = start
10        for num in nums:
11            if num-last_one <= 1 :
12                last_one = num
13            else: 
14                if start != last_one:
15                    ranges.append(f"{start}->{last_one}")
16                else: 
17                    ranges.append(str(start))
18                start = num
19                last_one = num
20        if start != last_one:
21            ranges.append(f"{start}->{last_one}")
22        else: 
23            ranges.append(str(start))
24        return ranges
25