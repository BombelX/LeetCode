# Last updated: 28.11.2025, 19:20:52
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not g:
            return 0
        if not s:
            return 0
        g.sort()
        g.reverse()
        s.sort()
        s.reverse()
        cnt = 0
        j = 0
        n=len(s)
        for i in range(len(g)):
            if j>=n:
                break
            if g[i]<=s[j]:
                cnt+=1
                j+=1
        return cnt
             