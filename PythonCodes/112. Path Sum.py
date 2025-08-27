# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node: Optional[TreeNode], target: int,sum_L: int) -> bool:
        if node:
            sum_L += node.val
            if self.helper(node.left, target, sum_L):
                return True
            if self.helper(node.right, target, sum_L):
                return True
            if not node.left and not node.right:
                if sum_L == target:
                    return True
            sum_L -= node.val
        return False
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.helper(root, targetSum,0)
