// Last updated: 14.03.2025, 21:33:01
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        i = 0
        j = 0
        max_length = 0
        chars = [0] * 256

        while j < n:
            if chars[ord(s[j])] == 0:
                chars[ord(s[j])] = 1
                j += 1
                max_length = max(max_length, j - i)
            else:
                chars[ord(s[i])] = 0
                i += 1

        return max_length
        