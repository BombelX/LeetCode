# Last updated: 30.11.2025, 23:27:46
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3
4        substr = ''
5        max_len = 0
6        left,right = 0,0
7        for letter in s:
8            if letter in substr:
9                max_len = max(right-left,max_len)
10                while letter  in substr:
11                    substr = substr.replace(s[left],'')
12                    left+=1
13            substr += letter
14            right += 1
15
16        max_len = max(right-left,max_len)   
17        return max_len
18            