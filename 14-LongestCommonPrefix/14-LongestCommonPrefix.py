class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = [201,""]
        for elem in strs :
            if len(elem)<shortest[0]:
                shortest[0],shortest[1] = len(elem),elem
        for i in range(shortest[0],0,-1):
            flag = False
            for el in strs:
                if el[0:i] != shortest[1][0:i]:
                    flag = True
                    break
            if not flag: return shortest[1][0:i]
        return ""