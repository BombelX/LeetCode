# Last updated: 28.11.2025, 21:31:27
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        def go(node):
10            if node is None:
11                return
12            node.left,node.right = node.right,node.left
13            go(node.left)
14            go(node.right)
15        go(root)
16        return root
17        