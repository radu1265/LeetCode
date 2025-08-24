# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        node = None
        output = []
        while queue:
            lvl = len(queue)
            temp = []
            for i in range(lvl):
                node = queue.pop(0)
                if node:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    temp.append(node.val)
            output.append(temp)
        return output
