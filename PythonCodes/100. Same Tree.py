# class TreeNode:
# Definition for a binary tree node.
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if q.val != p.val:
            return False
        queue_1, queue_2 = [], []
        queue_1.append(p)
        queue_2.append(q)

        while queue_1 and queue_2:
            node_1 = queue_1.pop()
            node_2 = queue_2.pop()

            if node_1.val != node_2.val:
                return False

            if node_1.left and node_2.left:
                queue_1.append(node_1.left)
                queue_2.append(node_2.left)
            elif node_1.left or node_2.left:
                return False

            if node_1.right and node_2.right:
                queue_1.append(node_1.right)
                queue_2.append(node_2.right)
            elif node_1.right or node_2.right:
                return False

        if queue_1 or queue_2:
            return False
        return True
