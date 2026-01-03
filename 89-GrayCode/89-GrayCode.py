# Last updated: 3.01.2026, 17:52:17
1from typing import List
2
3class Solution:
4    def to_gray(self, num):
5        binary = bin(num)[2:]
6        
7        gray_str = binary[0]
8        
9        for i in range(1, len(binary)):
10            if binary[i] == binary[i-1]:
11                gray_str += '0' 
12            else:
13                gray_str += '1'  
14                
15        return int(gray_str, 2)
16
17    def grayCode(self, n: int) -> List[int]:
18        res = []
19        for i in range(1 << n):
20            res.append(self.to_gray(i))
21        return res