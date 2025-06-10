# Last updated: 10.06.2025, 21:12:21
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        last_2  = 0
        last_1 = 1

        for i in range(n-2):
            tmp = last_1+last_2
            last_2 = last_1
            last_1 = tmp
        return last_1+last_2