# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS_preorder(self, root: Optional[TreeNode], out: List[int]) -> List[int]:
        if root:
            out.append(root.val)
            self.DFS_preorder(root.left, out)
            self.DFS_preorder(root.right, out)
        return out

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        return self.DFS_preorder(root, out)
