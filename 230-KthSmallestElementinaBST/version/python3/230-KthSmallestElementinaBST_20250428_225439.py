# Last updated: 28.04.2025, 22:54:39
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def kthSmallestRecur(root, cnt, k):
            if root is None:
                return -1
            left = kthSmallestRecur(root.left, cnt, k)
            if left != -1:
                return left
            cnt[0] += 1
            if cnt[0] == k:
                return root.val
            right = kthSmallestRecur(root.right, cnt, k)
            return right
        cnt = [0]
        return kthSmallestRecur(root, cnt, k)
