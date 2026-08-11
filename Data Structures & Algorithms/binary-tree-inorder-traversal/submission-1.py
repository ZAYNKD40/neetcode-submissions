# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        #recursion
        def traverse (curr):
            #base case
            if not curr:
                return
            #computation, going down left first until everything return nothing while in the process recording them with .append. inorder traversal so the .val at the start is in middle
            traverse(curr.left)
            res.append(curr.val)
            traverse(curr.right)
        traverse(root)
        return res

        