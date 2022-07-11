# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # recursive soln        
        # order = []
        # def dfs(root: Optional[TreeNode]):
        #     if (root is None): return
        #     dfs(root.left)
        #     order.append(root.val)
        #     dfs(root.right)
        # dfs(root)
        # return order
        
        # iterative solution
        current = root
        stack, order = [], []
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                order.append(current.val)
                current = current.right
            else:
                break
        return order
    