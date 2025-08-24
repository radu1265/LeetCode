# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = [root]
        depth = 0
        while queue:
            lvl = len(queue)
            node = None
            for i in range(lvl):
                node = queue.pop(0)
                if node:
                    if not node.left and not node.right:
                        return depth + 1
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            depth += 1
        return depth
