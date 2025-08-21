# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    @staticmethod
    def traverse(node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        return 1 + TreeNode.traverse(node.left) + TreeNode.traverse(node.right)
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return TreeNode.traverse(root)
