# Last updated: 10.12.2025, 21:50:36
1class Solution:
2    def minWindow(self, s: str, t: str) -> str:
3        if not s or not t: return ""
4        left = 0
5        min_len = float('inf')
6        min_idexes = (-1, -1)
7        cnr = {}
8        for letter in t:
9            if letter in cnr:
10                cnr[letter] += 1
11            else:
12                cnr[letter] = 1
13        
14        control_sum = len(t)
15        
16
17        for right in range(len(s)):
18            
19            if s[right] in cnr:
20                if cnr[s[right]] > 0:
21                    control_sum -= 1
22                cnr[s[right]] -= 1
23            
24            while control_sum == 0:
25                
26                current_len = right - left + 1
27                if min_len > current_len:
28                    min_len = current_len
29                    min_idexes = (left, right + 1) 
30                
31                if s[left] in cnr:
32                    cnr[s[left]] += 1
33                    if cnr[s[left]] > 0:
34                        control_sum += 1
35                
36                left += 1
37
38        if min_idexes[0] == -1:
39            return ""
40            
41        return s[min_idexes[0]:min_idexes[1]] 
42