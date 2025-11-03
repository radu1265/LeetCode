# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        max_zigzag = 0
        stack = [(root, 0, None)]  # (node, current_length, last_direction)

        while stack:
            node, cur_zigzag, last_dir = stack.pop()
            max_zigzag = max(max_zigzag, cur_zigzag)

            # Try to go left
            if node.left:
                if last_dir == 'R' or last_dir is None:
                    # Continue zigzag
                    stack.append((node.left, cur_zigzag + 1, 'L'))
                else:
                    stack.append((node.left, 1, 'L'))

            # Try to go right
            if node.right:
                if last_dir == 'L' or last_dir is None:
                    stack.append((node.right, cur_zigzag + 1, 'R'))
                else:
                    stack.append((node.right, 1, 'R'))

        return max_zigzag
