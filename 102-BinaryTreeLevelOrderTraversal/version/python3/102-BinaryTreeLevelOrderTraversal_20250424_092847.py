# Last updated: 24.04.2025, 09:28:47
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        queue = deque([root])
        sums = [0]*5000
        while queue:
            v = queue.popleft()
            leaf = True
            if v.right:
                leaf = False
                v.right.val += v.val
                queue.append(v.right)

            if v.left:
                leaf = False
                v.left.val += v.val
                queue.append(v.left)
            if leaf and v.val == targetSum:
                return True
        return False