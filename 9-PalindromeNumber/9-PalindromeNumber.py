# Last updated: 28.05.2025, 19:20:59
import math
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        num_len = math.floor(math.log10(x) + 1)
        while num_len > 1:
            if x % 10 == x // (10 ** (num_len - 1)):
                x = x % 10 ** (num_len - 1)
                x = x // 10
                num_len -= 2
            else:
                break
        if num_len <= 1:
            return True
        else:
            return False
