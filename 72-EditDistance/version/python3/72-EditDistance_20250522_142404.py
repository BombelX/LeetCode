# Last updated: 22.05.2025, 14:24:04
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        history = {}

        def decode(s, sub):
            if s == '':
                return 1
            elif s[0] == '0':
                return 0

            if (s, sub) in history:
                return history[(s, sub)]
            summ = 0
            summ += decode(s[1:], 0)
            if len(s) >= 2:
                two = int(s[:2])
                if 10 <= two <= 26:
                    summ += decode(s[2:], two)
            history[(s, sub)] = summ
            return summ

        return decode(s, 0)