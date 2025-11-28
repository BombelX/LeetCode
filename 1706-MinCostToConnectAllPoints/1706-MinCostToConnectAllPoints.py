# Last updated: 28.11.2025, 19:20:44
from math import *
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def generate_edges(points):
            edges = []
            for x in range(len(points)):
                for y in range(x+1,len(points)):
                    w = abs(points[x][0]-points[y][0])+abs(points[x][1]-points[y][1])
                    edges.append([x,y,w])
            return edges
        class Node:
            def __init__(self, val):
                self.val = val
                self.parent = self      
                self.rank = 0           
        def find(x):
            if x.parent is not x:
                x.parent = find(x.parent)   # kompresja ścieżki
            return x.parent

        def union(x, y):
            xroot = find(x)
            yroot = find(y)
            if xroot is yroot:
                return
            if xroot.rank < yroot.rank:
                xroot.parent = yroot
            elif xroot.rank > yroot.rank:
                yroot.parent = xroot
            else:
                yroot.parent = xroot
                xroot.rank += 1

        def MST(n, edges):
            ver = [Node(i) for i in range(n)]
            edges.sort(key=lambda e: e[2])
            wynik = 0
            for u, v, w in edges:
                if find(ver[u]) is not find(ver[v]):
                    union(ver[u], ver[v])
                    wynik+=w
            return wynik

        edges = generate_edges(points)
        if len(edges) == 1:
            return edges[0][2]

        res = MST(len(edges),edges)
        return res