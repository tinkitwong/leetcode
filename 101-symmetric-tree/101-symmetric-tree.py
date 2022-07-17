# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True
        return self.isMirror(root.left, root.right)
        
    def isMirror(self, left_root, right_root) -> bool:
        # if left_root and right_root exists
        if left_root and right_root: 
            return left_root.val == right_root.val and self.isMirror(left_root.left, right_root.right) and self.isMirror(left_root.right, right_root.left)
        return left_root == right_root