class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            x = int(str(abs(x))[::-1])
            x = -x
            if x<-2**31-1:
                return 0 
            else:
                return x
        else:
            x = int(str(abs(x))[::-1])
            if x>2**31:
                return 0
            else:
                return x
            