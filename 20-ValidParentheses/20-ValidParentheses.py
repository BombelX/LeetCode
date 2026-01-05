# Last updated: 5.01.2026, 18:45:32
1from collections import deque
2
3class Solution:
4    def isValid(self, s: str) -> bool:
5        stack = deque()
6
7        for bracket in s:
8            if bracket == '(' or bracket == '[' or bracket == '{':
9                stack.append(bracket)
10            else:
11                if not stack:
12                    return False
13                b = stack.pop()
14                if b == '(' and bracket == ')':
15                    continue
16                elif b == '{' and bracket == '}':
17                    continue
18                elif b == '[' and bracket == ']':
19                    continue
20                else:
21                    return False
22        if stack:
23            return False
24        return True
25
26