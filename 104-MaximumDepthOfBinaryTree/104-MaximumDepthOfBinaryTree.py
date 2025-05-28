# Last updated: 28.05.2025, 19:20:35
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def bfs(v):
            v.val = [v.val,0]
            dist = [[v.val[0]]]
            queue = deque()
            queue.append(v)
            while queue:
                ver = queue.popleft()
                if ver.left:
                    ver.left.val = [ver.left.val,ver.val[1]+1]  
                    if len(dist)<= ver.left.val[1]:
                        dist.append([ver.left.val[0]])
                    else:
                        dist[ver.left.val[1]].append(ver.left.val[0])

                    queue.append(ver.left)

                if ver.right:
                    ver.right.val = [ver.right.val,ver.val[1]+1]  
                    if len(dist)<= ver.right.val[1]:
                        dist.append([ver.right.val[0]])
                    else:
                        dist[ver.right.val[1]].append(ver.right.val[0])
                    queue.append(ver.right)
            return dist
        return len(bfs(root))
