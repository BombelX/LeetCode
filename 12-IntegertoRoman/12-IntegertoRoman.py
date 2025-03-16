import math
class Solution:
    

    def intToRoman(self, num: int) -> str:
        def find_nearest(num):
            roman_val = [(1000,'M'),(500,'D'),(100,'C'),(50,'L'),(10,'X'),(5,'V'),(1,'I')]
            i = 0
            for i in range(7):
                if num//roman_val[i][0]>0:
                    return i


        roman_val = [(1000,'M'),(500,'D'),(100,'C'),(50,'L'),(10,'X'),(5,'V'),(1,'I')]
        res = ""
        while num>0:
            num_len = int(math.log10(num))+1
            if num//10**(num_len-1) == 4 :
                ind = find_nearest(num)
                res+= roman_val[ind][1]+roman_val[ind-1][1]
                num -= (roman_val[ind-1][0]-roman_val[ind][0])
            elif num//10**(num_len-1) == 9:
                ind = find_nearest(num)
                res+= roman_val[ind+1][1]+roman_val[ind-1][1]
                num -= (roman_val[ind-1][0]-roman_val[ind+1][0])
            else:
                ind = find_nearest(num)
                res += roman_val[ind][1]

                num -= roman_val[ind][0]
        return res

            
            