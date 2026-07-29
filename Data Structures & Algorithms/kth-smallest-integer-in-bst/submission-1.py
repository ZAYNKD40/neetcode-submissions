# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #kth smallest
        #main problem to overcome:
        #dont know how many nodes are in a tree so definitely have to traverse entire tree
        #if have to sort them after too that would be nlogn
        res=[]
        #traverse entire node and append to res
        #try sorting approach first
        
        def dfs(node): #what do I pass in the dfs? what operations in dfs to travel the whole thing?
            #base case, what does the base case look like?
             #what do I return here? it is dfs so I need to go back to the right? is going to all left first ehn all right second how dfs work?
            if not node:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)


        dfs(root)
        res.sort()
        print(res)
        return res[k-1]
        
        