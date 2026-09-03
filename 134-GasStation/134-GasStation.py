# Last updated: 3.09.2026, 21:33:12
1class Solution:
2    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
3        letters_cnt = 26*[0]
4
5        for letter in magazine:
6            letters_cnt[ord(letter)%26] += 1
7        
8        for letter in ransomNote:
9            letters_cnt[ord(letter)%26] -= 1
10        
11        for c in letters_cnt:
12            if c < 0:
13                return False
14
15        return True
16