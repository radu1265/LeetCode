# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node: Optional[TreeNode], target: int, sum_L: int, path: List[int], paths: List[List[int]]) -> List[List[int]]:
        if node:
            path.append(node.val)
            sum_L += node.val
            self.helper(node.left, target, sum_L, path, paths)
            self.helper(node.right, target, sum_L, path, paths)
            if not node.left and not node.right:
                if sum_L == target:
                    paths.append(path.copy())
            sum_L -= node.val
            path.pop()
        return paths
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        return self.helper(root, targetSum, 0, [], [])
