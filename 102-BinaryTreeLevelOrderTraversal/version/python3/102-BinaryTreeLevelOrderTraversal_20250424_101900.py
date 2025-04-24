# Last updated: 24.04.2025, 10:19:00
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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        res = []
        queue = deque([root])
        cnt = 0
        level = 0
        lvl = []
        while queue:
            cnt+=1
            if cnt > 2**level:
                level +=1
                n = len(lvl)
                for i in range(n):
                    if i == n-1:
                        lvl[i].next = None
                    else:
                        lvl[i].next = lvl[i+1]
                cnt = 1
                lvl = []
            v = queue.popleft()
            lvl.append(v)
            if v.left:
                queue.append(v.left)
            if v.right:
                queue.append(v.right)
        n = len(lvl)
        for i in range(n):
            if i == n-1:
                lvl[i].next = None
            else:
                lvl[i].next = lvl[i+1]

        #for lvl in lvls:
        #    n = len(lvl)
        #    for i in range(n):
        #        print(lvl[i].val)
        #        if i == n-1:
        #            lvl[i].next = None
        #        else:
        #            lvl[i].next = lvl[i+1]
        #    print("--------------")
        return root