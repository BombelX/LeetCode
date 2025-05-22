# Last updated: 22.05.2025, 14:46:39
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]
        numRows = rowIndex+1
        for row in range(1,numRows):
            new_row = [0]*(row+1)
            new_row[0] = 1
            new_row[-1] = 1
            for i in range(1,row):
                
                new_row[i] = res[row-1][i-1]+res[row-1][i]
            res.append(new_row)
        return res[rowIndex]