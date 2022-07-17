# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root,1]]
        res = 0
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(depth, res)
                stack.extend([[node.left, depth+1], [node.right, depth+1]])
        return res