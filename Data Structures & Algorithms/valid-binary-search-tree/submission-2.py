# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #search in pair of three, if parents and children match go onto next.
        #we also want to make sure all nums on right of root is bigger than root and vice versa
        #so save like a difference between current and its parent for the children? or maybe just do saving the parent before
        #dfs recursion approach
        def valid(node, left, right): #left and right here is not the node but the comparison like check if 5<4<7 if not not valid this is one of the false case
            #base case
            if not node:
                return True
            if not (node.val < right and node.val > left): #remember the parenthesis
                return False # a node that broke the bst
            #making recursive calls, make sure left and right subtree is valid
            #node.val is saving the parent
            return valid(node.left, left, node.val) and valid(node.right, node.val, right) #going back to the 5<4<7 example, this right and left is the number comparison, if you are going right, your node.val should be on the left
            #make sure the entire subtree is valid so return both
        return valid(root, float("-inf"), float("inf")) #pass in the root value and need to compare it to something since recursion passing
            #that is why using -inf and inf for the left and right


        