# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS_postorder(self, root: Optional[TreeNode], out:List[int]) -> List[int]:
        if root:
            self.DFS_postorder(root.left, out)
            self.DFS_postorder(root.right, out)
            out.append(root.val)
        return out

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        return self.DFS_postorder(root, out)
