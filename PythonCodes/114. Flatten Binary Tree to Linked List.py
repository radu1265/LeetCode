# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_leaf(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        while node.right:
            node = node.right
        return node

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root:
            if root.left:
                aux = root.right
                root.right = root.left
                node = self.get_leaf(root.right)
                node.right = aux
                root.left = None
            self.flatten(root.right)
