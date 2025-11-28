# Last updated: 28.11.2025, 19:20:55
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


        