# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False

        tree_left, tree_right = root.left, root.right
        queue_left, queue_right = [tree_left], [tree_right]
        
        while queue_left and queue_right:
            tree_left = queue_left.pop()
            tree_right = queue_right.pop()

            if tree_left.val != tree_right.val:
                return False
            
            if tree_left.left and tree_right.right:
                queue_left.append(tree_left.left)
                queue_right.append(tree_right.right)
            elif tree_left.left or tree_right.right:
                return False

            if tree_left.right and tree_right.left:
                queue_left.append(tree_left.right)
                queue_right.append(tree_right.left)
            elif tree_left.right or tree_right.left:
                return False
        return True
