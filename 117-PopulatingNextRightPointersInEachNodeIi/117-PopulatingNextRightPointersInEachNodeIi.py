# Last updated: 28.05.2025, 19:20:29
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        res = []
        queue = deque([root])
        cnt = 0
        level = 0
        lvl = []
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                v = queue.popleft()
                lvl.append(v)
                if v.left:
                    queue.append(v.left)
                if v.right:
                    queue.append(v.right)
            for i in range(level_size):
                if i == level_size-1:
                    lvl[i].next = None
                else:
                    lvl[i].next = lvl[i+1]
            lvl = []


        return root