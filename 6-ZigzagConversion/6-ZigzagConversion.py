class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        else:
            priod = numRows*2 -2
        t = [""]*numRows
        tmp = 0
        for i in range(len(s)):
            if i%priod <numRows:
                t[i%priod] += s[i]
                tmp = numRows-2
            else:
                t[tmp] += s[i]
                tmp-=1
        res = ""
        for elem in t:
            res+=elem
        return res
            