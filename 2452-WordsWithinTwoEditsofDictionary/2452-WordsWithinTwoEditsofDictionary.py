# Last updated: 22.04.2026, 23:28:38
1class Solution:
2    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
3        res = []
4        for dict_ind , query in enumerate(queries):
5            for dict_ in dictionary:
6                err = 0
7                for i in range(len(query)):
8                    if err>2:
9                        break
10                    if query[i] != dict_[i]:
11                        err+=1
12                if err <= 2:
13                    res.append(query)
14                    break
15        return res
16
17
18
19
20        