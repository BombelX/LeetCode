# Last updated: 22.05.2025, 14:44:55
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for row in range(1,numRows):
            new_row = [0]*(row+1)
            new_row[0] = 1
            new_row[-1] = 1
            for i in range(1,row):
                
                new_row[i] = res[row-1][i-1]+res[row-1][i]
            res.append(new_row)
        return res

