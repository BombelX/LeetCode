# Last updated: 28.05.2025, 19:20:46
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(0,len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1