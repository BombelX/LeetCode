# Last updated: 28.11.2025, 19:21:05
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         n = len(prices)
#         diffrences = [0]*len(prices)
#         for i in range(1,n):
#             diffrences[i] = prices[i]-prices[i-1]
#         tab = []
#         summ = 0
#         for diff in diffrences:
#             if diff<0:
#                 tab.append(summ)
#                 summ=0
#             else:
#                 summ+=diff
#         tab.append(summ)
#         if len(tab) == 1:
#             return tab[0]
#         maks1,maks2 = 0,0
#         for elem in tab:
#             if elem>maks1:
#                 maks2 = maks1
#                 maks1 = elem
#             elif elem > maks2:
#                 maks2 = elem
#         return maks1+maks2

class Solution:
    def maxProfit(self,prices: list[int]) -> int:
        hold1 = hold2 = float('-inf')   # ile mamy po kupnie
        rel1  = rel2  = 0               # ile mamy po sprzedaży

        for p in prices:
            rel2  = max(rel2,  hold2 + p)    # sprzedaj drugą
            hold2 = max(hold2, rel1  - p)    # kup drugą
            rel1  = max(rel1,  hold1 + p)    # sprzedaj pierwszą
            hold1 = max(hold1,     - p)      # kup pierwszą
        return rel2