class Solution:
    def longestValidParentheses(self, s: str) -> int:
        opened = 0
        closed = 0
        longe = 0
        if ")" not in s or "(" not in s:
            return 0
        for j in range(0,len(s)):
            longest = 0
            opened = 0
            closed = 0
            for i in range(j,len(s)):
                if s[i] == "(":
                    opened += 1
                elif ")" and closed<opened:
                    closed += 1
                else:
                    break
                
                if opened == closed:
                    longest = i-j+1
            longe = max(longest,longe)
        return longe

