# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        nodes = [(root, root.val)]
        good_nodes = 0

        while nodes:
            node, max_so_far = nodes.pop()

            if node.val >= max_so_far:
                good_nodes += 1
            
            if node.right:
                nodes.append((node.right, max(max_so_far, node.val)))

            if node.left:
                nodes.append((node.left, max(max_so_far, node.val)))

        
        return good_nodes

            
