# Last updated: 16.04.2025, 09:33:01
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        p = root.left
        q = root.right

        if not p and not q:
            return True
        elif not p or not q:
            return False
        visited_p = [0]*100
        visited_q = [0]*100
        visited_p[0],visited_q[0] = 2,2
        q1 = deque([p])
        q2 = deque([q])
        while q1 and q2:
            v1,v2 = q1.pop(),q2.pop()
            if v1.val != v2.val:
                return False
            tab = [0,0,0,0]
            if v1.left:
                tab[0] = 1
            if v2.left:
                tab[1] = 1
            if v1.right:
                tab[2] = 1
            if v2.right:
                tab[3] = 1
            if tab[1]+tab[2] == 1:
                return False
            elif tab[1]+tab[2] == 2:
                q1.append(v1.right)
                q2.append(v2.left)
            if tab[0]+tab[3] == 1:
                return False
            elif tab[3]+tab[0] == 2:
                q1.append(v1.left)
                q2.append(v2.right)
            
        return True
