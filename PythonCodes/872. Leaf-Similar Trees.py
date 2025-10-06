# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS (self, node: Optional[TreeNode]) -> List[int]:
        if node:
            if not node.left and not node.right:
                return [node.val]
            return self.DFS(node.left) + self.DFS(node.right)
        return []

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.DFS(root1) == self.DFS(root2)
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def DFS_leafSimilar(self, node: Optional[TreeNode]) -> List[int]:
#         visited = set()
#         nodes = [node]
#         leaf_seq = []
#         while nodes:
            
#             node = nodes.pop()
#             if node in visited:
#                 cotinue

#             visited.add(node)
#             if node.right and node.right not in visited:
#                 nodes.append(node.right)

#             if node.left and node.left not in visited:
#                 nodes.append(node.left)

#             if not node.left and not  node.right:
#                 leaf_seq.append(node.val)

#         return leaf_seq

#     def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
#         return self.DFS_leafSimilar(root1) == self.DFS_leafSimilar(root2)
