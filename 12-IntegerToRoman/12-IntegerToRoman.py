# Last updated: 28.05.2025, 19:20:58
import math
class Solution:
    

    def intToRoman(self, num: int) -> str:
        values = [
            ('M', 1000), 
            ('CM', 900),
            ('D', 500),
            ('CD', 400),
            ('C', 100),
            ('XC', 90),
            ('L', 50), 
            ('XL', 40),
            ('X', 10), 
            ('IX', 9),
            ('V', 5), 
            ('IV', 4),
            ('I', 1)
        ]

        ans = []
        for symbol, val in values:
            if num == 0:
                break
            count, num = divmod(num, val)
            ans.append(symbol * count)

        return ''.join(ans)
        # def find_nearest(num):
        #     roman_val = [(1000,'M'),(500,'D'),(100,'C'),(50,'L'),(10,'X'),(5,'V'),(1,'I')]
        #     i = 0
        #     for i in range(7):
        #         if num//roman_val[i][0]>0:
        #             return i


        # roman_val = [(1000,'M'),(500,'D'),(100,'C'),(50,'L'),(10,'X'),(5,'V'),(1,'I')]
        # res = ""
        # while num>0:
        #     num_len = int(math.log10(num))+1
        #     if num//10**(num_len-1) == 4 :
        #         ind = find_nearest(num)
        #         res+= roman_val[ind][1]+roman_val[ind-1][1]
        #         num -= (roman_val[ind-1][0]-roman_val[ind][0])
        #     elif num//10**(num_len-1) == 9:
        #         ind = find_nearest(num)
        #         res+= roman_val[ind+1][1]+roman_val[ind-1][1]
        #         num -= (roman_val[ind-1][0]-roman_val[ind+1][0])
        #     else:
        #         ind = find_nearest(num)
        #         res += roman_val[ind][1]

        #         num -= roman_val[ind][0]
        # return res

            
            