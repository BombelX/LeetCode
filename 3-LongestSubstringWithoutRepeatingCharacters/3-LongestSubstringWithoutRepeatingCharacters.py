class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        s_len = len(s)

        longest = 0
        for str in range(0,s_len):
            curr_len = 0
            tab = [False]*256
            
            for i in range(str,s_len):
                if tab[ord(s[i])] == True:
                    
                    longest = max(curr_len,longest)
                    break
                else:
                    tab[ord(s[i])] = True
                    curr_len += 1
            longest = max(curr_len,longest)

        return longest

