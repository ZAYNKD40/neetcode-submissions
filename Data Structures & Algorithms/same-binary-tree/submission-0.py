# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #dfs method
        if not p and not q: #when null and at the end
            return True 
        if p and q and p.val == q.val: #compare left and right node, 
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else: #if one side is null only or if they dont match val
            return False
        