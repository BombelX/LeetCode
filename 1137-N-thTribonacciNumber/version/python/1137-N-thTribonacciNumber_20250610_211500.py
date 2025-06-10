# Last updated: 10.06.2025, 21:15:00
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        last_3 = 0
        last_2  = 1
        last_1 = 1

        for i in range(n-3):
            tmp = last_1+last_2+last_3
            last_3 = last_2
            last_2 = last_1
            last_1 = tmp
        return last_1+last_2+last_3