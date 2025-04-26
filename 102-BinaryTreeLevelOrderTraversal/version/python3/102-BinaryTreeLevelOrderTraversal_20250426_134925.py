# Last updated: 26.04.2025, 13:49:25
from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        queue = deque([n])
        visited = {n}
        level = 0  

        while queue:
            level += 1
            for _ in range(len(queue)):
                curr = queue.popleft()
                for sq in squares:
                    nxt = curr - sq
                    if nxt == 0:
                        return level
                    if nxt < 0:
                        break
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)
        return level
