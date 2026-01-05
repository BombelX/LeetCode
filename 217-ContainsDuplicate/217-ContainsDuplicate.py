# Last updated: 5.01.2026, 18:27:44
1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        meeted = set()
4        for num in nums:
5            if num in meeted:
6                return True
7            meeted.add(num)
8        return False