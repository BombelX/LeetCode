class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def isValid(s: str) -> bool:
            brack = {
                "(":")",
                "[":"]",
                "{":"}"

            }
            open_brackets = []
            for bracket in s:
                if bracket in "({[":
                    open_brackets.append(bracket)
                else:
                    if len(open_brackets) == 0 :return False
                    if bracket == brack[open_brackets[-1]]:
                        open_brackets.pop()
                    else:
                        return False
            if  len(open_brackets) == 0:
                return True
            return False
        def generate_rec(res,n):
            if n == 0:
                if isValid(res):
                    result.append(res)
                return
            else:
                generate_rec(res+")",n-1)
                generate_rec(res+"(",n-1)
        generate_rec("",n*2)
        return result
            
