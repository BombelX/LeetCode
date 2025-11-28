# Last updated: 28.11.2025, 21:27:58
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8from collections import deque 
9class Solution:
10    def maxDepth_bfs(self, root: Optional[TreeNode]) -> int:
11        if root is None:
12            return 0
13        priority_queue = deque([(root, 1)]) 
14        max_dp = 0
15        while priority_queue:
16            node,deep = priority_queue.popleft()
17            if node.left:
18                priority_queue.append([node.left,deep+1])
19            if node.right:
20                priority_queue.append([node.right,deep+1])
21            max_dp = max(max_dp,deep)
22        return max_dp
23    def maxDepth(self, root: Optional[TreeNode]) -> int:
24        def dfs(node):
25            if node is None:
26                return 0
27            return max(dfs(node.left),dfs(node.right))+1  
28        return dfs(root)        
29