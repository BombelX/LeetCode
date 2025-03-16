class Solution:



    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        res = []
        pattert = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        def recursivly_generate_permutation(word,r_digits):
            if r_digits == "":
                res.append(word)
                return
            act = r_digits[0]
            r_digits = r_digits[1:]
            options = pattert[int(act)]
            for option in options:
                recursivly_generate_permutation(word+option,r_digits)

        digits.replace('1',"")
        recursivly_generate_permutation("",digits)
        return res

        
