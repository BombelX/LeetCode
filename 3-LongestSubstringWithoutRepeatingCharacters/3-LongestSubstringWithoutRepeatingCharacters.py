# Last updated: 30.11.2025, 23:32:34
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        char_index_map = {} 
4        left = 0
5        max_len = 0
6        
7        for right, char in enumerate(s):
8            if char in char_index_map and char_index_map[char] >= left:
9                left = char_index_map[char] + 1
10            char_index_map[char] = right
11            max_len = max(max_len, right - left + 1)
12            
13        return max_len