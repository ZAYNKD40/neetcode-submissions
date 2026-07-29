# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: #by definition, an empty tree is also a subtree
            return True
        if not root:
            return False
        if self.sameTree(root, subRoot): #end of our check
            return True
        #keep checking each node for the same subroot down each node and each children essentially doing same tree check per node
        return(self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def sameTree(self, r, s):
        if not r and not s: #if they pass all checks and we are on Null
            return True
        if r and s and r.val == s.val:
            return (self.sameTree(r.left, s.left) and
                self.sameTree(r.right, s.right))
        return False
            





        