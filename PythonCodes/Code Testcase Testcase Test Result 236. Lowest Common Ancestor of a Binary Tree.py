# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getPathToNode(self,  root: 'TreeNode', node: 'TreeNode') -> List[int]:
        if not root:
            return None

        stack = [(root, [root])]

        while stack:
            cur_node, parent_list = stack.pop()

            if cur_node == node:
                return parent_list

            if cur_node.left:
                stack.append((cur_node.left, parent_list + [cur_node.left]))
            if cur_node.right:
                stack.append((cur_node.right, parent_list + [cur_node.right]))
        return None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_list = self.getPathToNode(root, p)
        q_list = self.getPathToNode(root, q)
        lca = None

        for node_p, node_q in zip(p_list, q_list):
            if node_p == node_q:
                lca = node_p
        return lca
