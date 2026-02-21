# Last updated: 21.02.2026, 21:00:14
from typing import List
from functools import cmp_to_key

class Solution:

    def comparator(self, a: int, b: int) -> int:
        ab = str(a) + str(b)
        ba = str(b) + str(a)
        if ab > ba:   # a ma być wcześniej
            return -1
        if ab < ba:
            return 1
        return 0

    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(key=cmp_to_key(self.comparator))
        res =  ''.join(map(str, nums))
        res = res.lstrip('0')
        if len(res) == 0:
            return '0'
        else:
            return res