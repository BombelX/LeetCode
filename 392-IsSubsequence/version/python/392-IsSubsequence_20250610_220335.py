# Last updated: 10.06.2025, 22:03:35
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n==0 and m == 0:
            return True
        elif n == 0:
            return True
        elif m == "":
            return False
        else:
            actual = 0
            for letter in t:
                if letter == s[actual]:
                    actual+=1
                    if actual == n:
                        return True
            return False


        