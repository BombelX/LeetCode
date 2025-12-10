# Last updated: 10.12.2025, 18:19:56
1class NumArray:
2    prefix_sum = []
3    nums = []
4    def __init__(self, nums: List[int]):
5        self.prefix_sum = [0] 
6        for num in nums:
7            self.prefix_sum.append(self.prefix_sum[-1] + num)
8
9    def sumRange(self, left: int, right: int) -> int:
10        return self.prefix_sum[right + 1] - self.prefix_sum[left]
11# Your NumArray object will be instantiated and called as such:
12# obj = NumArray(nums)
13# param_1 = obj.sumRange(left,right)