# Last updated: 28.11.2025, 19:21:16
from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # --------- 1. silnia (tak jak u Ciebie) ------------------------------
        sil_tab = [1]
        def silnia(x: int) -> int:
            nonlocal sil_tab
            if x < len(sil_tab):
                return sil_tab[x]
            res = sil_tab[-1]
            for i in range(len(sil_tab), x + 1):
                res *= i
                sil_tab.append(res)
            return res

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # start albo meta zablokowane → 0 dróg
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        # --------- 2. zbierz i posortuj przeszkody --------------------------
        obstacles = [(r, c)
                     for r in range(m)
                     for c, v in enumerate(obstacleGrid[r])
                     if v == 1]
        obstacles.sort(key=lambda p: p[0] + p[1])          # rosnąco po r+c

        # --------- 3. pomocnicza liczba kombinacji --------------------------
        def C(a: int, b: int) -> int:                       # (a choose b)
            return silnia(a) // (silnia(b) * silnia(a - b))

        # --------- 4. f(k): ścieżki do k-tej przeszkody ---------------------
        good_to_obs = []                                    # f(k) z opisu
        for idx, (r, c) in enumerate(obstacles):
            ways = C(r + c, r)                              # wszystkie do (r,c)
            for (pr, pc), prev in zip(obstacles, good_to_obs):
                if pr <= r and pc <= c:                     # leży "po drodze"
                    ways -= prev * C((r - pr) + (c - pc), r - pr)
            good_to_obs.append(ways)                        # f(idx)

        # --------- 5. ścieżki bez przeszkód minus te "złe" ------------------
        total = C(m + n - 2, m - 1)                         # wszystkie do mety
        for (r, c), bad in zip(obstacles, good_to_obs):
            total -= bad * C((m - 1 - r) + (n - 1 - c), m - 1 - r)

        return total
