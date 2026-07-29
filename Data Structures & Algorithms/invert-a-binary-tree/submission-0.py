# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #using dfs and recursion, invert the tree
        # base case
        if not root:
            return None
        
        #swap left and right but because the swap one value is not linked anymore so need to keep track of it
        tmp = root.left
        root.left = root.right
        root.right = tmp

        #calling the recursion
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        