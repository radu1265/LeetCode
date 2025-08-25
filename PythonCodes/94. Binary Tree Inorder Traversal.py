# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS (self, root: Optional[TreeNode], out: List[int]) -> List[int]:
        if root:
            self.DFS(root.left, out)
            out.append(root.val)
            self.DFS(root.right, out)
        return out
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        return self.DFS(root, out)
