# Last updated: 9.12.2025, 20:21:48
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        
4        for i,x in enumerate(strs):
5            y = sorted(x)
6            strs[i] = (y,x)
7        strs = sorted(strs, key = lambda x:x[0])
8        output = []
9        i = 0
10        act = strs[0][0]
11        substr = []
12        for sub in strs:
13            if sub[0] == act:
14                substr.append(sub[1])
15            else:
16                output.append(substr[::1])
17                substr = [sub[1]]
18                act = sub[0]
19        output.append(substr)
20        return output