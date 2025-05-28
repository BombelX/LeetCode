# Last updated: 28.05.2025, 19:20:56
class Solution:
    def romanToInt(self, s: str) -> int:
        special = ['IV','IX','XL','XC','CD','CM']
        roman = {
            "M":1000,
            "D":500,
            "C":100,
            "L":50,
            "X":10,
            "V":5,
            "I":1
        }
        res = 0
        flag = False
        for i in range(len(s)):
            if flag:
                flag = False
                continue
            if i+1<len(s):
                act = s[i]
                nxt = s[i+1]
                if act+nxt in special:
                    flag = True
                    res+=roman[nxt]-roman[act]
                    continue

            res+=roman[s[i]]
        return res




            
        