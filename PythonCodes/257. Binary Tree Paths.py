# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node: Optional[TreeNode], paths: List[str], path: str) -> List[str]:
        if node:
            path = f"{path}->{node.val}"
            self.helper(node.left, paths, path)
            self.helper(node.right, paths, path)
            if not node.left and not node.right:
                paths.append(path[2:])
                path = path[:-1]
        return paths

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = self.helper(root, [], '')

        return paths
