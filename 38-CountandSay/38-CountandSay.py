# Last updated: 5.01.2026, 15:41:07
1class Solution:
2    def countAndSay(self, n: int) -> str:
3        def RLE(num):
4            new = ''
5            cnt = 0
6            last = ''
7            for i in num:
8                if i == last:
9                    cnt += 1
10                else:
11                    new += f'{cnt}'+last
12                    last = i
13                    cnt = 1
14            new += f'{cnt}'+last
15            return new
16
17        x = '1'
18        for i in range(1,n):
19            x = RLE(x)[1:]
20        return x