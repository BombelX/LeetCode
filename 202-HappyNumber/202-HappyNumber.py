# Last updated: 10.12.2025, 22:18:57
1class Solution:
2    def isHappy(self, n: int) -> bool:
3        def get_next(x):
4            next_num = 0
5            while x>0:
6                next_num += (x%10)**2
7                x = x//10
8            return next_num
9        
10
11        rabbit = get_next(get_next(n))
12        turtle = n
13        while rabbit != turtle:
14            rabbit = get_next(get_next(rabbit))
15            turtle = get_next(turtle)
16        
17        return rabbit == 1