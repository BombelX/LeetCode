# Last updated: 28.11.2025, 20:03:25
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        if len(s) != len(t): return False
4        letters = {}
5        for letter in s:
6            if letter in letters.keys():
7                letters[letter] +=1
8            else:
9                letters[letter] = 1
10        for letter in t:
11            if letter in letters.keys():
12                letters[letter] -= 1
13                if letters[letter] == -1:
14                    return False
15            else:
16                return False
17        return True