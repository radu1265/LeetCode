# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS (self, node: Optional[TreeNode]) -> int:
        if node:
            max_left = self.DFS(node.left)
            max_right = self.DFS(node.right)
            return max(max_left, max_right) + 1
        return 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.DFS(root)
