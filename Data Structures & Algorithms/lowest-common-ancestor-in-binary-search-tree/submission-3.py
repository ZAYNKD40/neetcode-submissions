# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        while curr: # tree traverse and compare values, since this is a binary search tree, less to left more to right
            if p.val > curr.val and q.val > curr.val: #too small, go right
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val: #too big, go left
                curr = curr.left
            else:
                return curr 
        #guaranteed the two nodes will be in the bst
        #this is a BST, the two value have to be both larger or both smaller, everything
        #smaller than the origin number on left side and vice versa for right
        #so need to both be same to pull down, this is solved with the nature of BST


        