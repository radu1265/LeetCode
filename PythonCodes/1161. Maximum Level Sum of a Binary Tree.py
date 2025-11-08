# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        lvl = 1
        queue.append((root, lvl))
        max_lvl_sum = (root.val, lvl)
        aux_lvl_sum = 0

        while queue:
            node, aux_lvl = queue.popleft()

            if aux_lvl == lvl:
                aux_lvl_sum += node.val
            else:
                if max_lvl_sum[0] < aux_lvl_sum:
                    max_lvl_sum = (aux_lvl_sum, lvl)
                    
                lvl = aux_lvl
                aux_lvl_sum = node.val
            
            if node.left:
                queue.append((node.left, aux_lvl + 1))

            if node.right:
                queue.append((node.right, aux_lvl + 1))

        if max_lvl_sum[0] < aux_lvl_sum:
            return aux_lvl
        return max_lvl_sum[1]
