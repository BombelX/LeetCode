# Last updated: 23.04.2025, 10:23:59
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

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
        dist = bfs(root)
        res = []
        for i,elem in enumerate(dist):
            if i%2 == 1:
                elem.reverse()
            res.append(elem)
        return res