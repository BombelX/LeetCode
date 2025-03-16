class Solution:
    def isValid(self, s: str) -> bool:
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
            