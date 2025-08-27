# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def from_list_to_num(self, path: List[int]) -> int:
        s = ''
        for elem in path:
            s += str(elem)
        return int(s)
    def helper(self, node: Optional[TreeNode], path: List[int], paths: List[int]) -> List[int]:
        if node:
            path.append(node.val)
            self.helper(node.left, path, paths)
            self.helper(node.right, path, paths)
            if not node.left and not node.right:
                path_joined = self.from_list_to_num(path)
                paths.append(path_joined)
            path.pop()
        return paths
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return sum(self.helper(root, [], []))
