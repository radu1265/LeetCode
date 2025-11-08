# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        lvl = 0
        right_side = {lvl : root.val}
        queue = deque()
        queue.append((root, lvl))

        while queue:
            node, lvl = queue.pop()
            # add/ change the value in the dict
            right_side[lvl] = node.val
            if node.right:
                queue.append((node.right, lvl + 1))
            if node.left:
                queue.append((node.left, lvl + 1))
        return list(right_side.values())
