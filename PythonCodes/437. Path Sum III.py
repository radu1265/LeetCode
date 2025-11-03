# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self, node: Optional[TreeNode], targetSum: int) -> int:
        stack = [(node, node.val)]
        options = 0

        while stack:
            cur_node, cur_sum = stack.pop()
            if cur_sum == targetSum:
                options += 1
            if cur_node.left:
                stack.append((cur_node.left, cur_sum + cur_node.left.val))
            if cur_node.right:
                stack.append((cur_node.right, cur_sum + cur_node.right.val))
        return options
            
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # BFS
        queue = deque([root])
        good_paths = 0

        while queue:
            node = queue.popleft()
            if not node:
                continue
            
            # apply dfs
            good_paths += self.DFS(node, targetSum)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return good_paths
