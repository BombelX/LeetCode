# Last updated: 28.05.2025, 19:20:34
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        if root is None:
            return result
        
        queue = []
        queue.append(root)

        while queue:
            level = []
            size = len(queue)

            for i in range(0, size):
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.insert(0, level)

        return result
