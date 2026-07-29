# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #can do bfs or dfs
        #bfs using queue, the first in will be the node and after you get the children remove the node that was in first FIFO
        #when you remove add it to a sublist of its level
        res = [] 

        q = collections.deque()
        q.append(root)
        while q: #if q is not empty there are nodes with potential children to be checked
            qLen = len(q) #iterate through one level at a time
            level = [] #level list to add to result list
            for i in range(qLen): #for the nodes needed to be checked
                node = q.popleft() #the current node we are checking children and pop in same time
                if node:
                    level.append(node.val) #level of current node starting with the first
                    q.append(node.left) #append the left and right node to the q to be checked and they are the next level
                    q.append(node.right)#also if the node is null q will be added None, not nothing and for the queue we only check when it is not null so when null it is the end of that branch
            if level: #if the level is non empty add to result, since for loop goes through all the queue the for loop handle the horizontal entire level for the tree while the while loop handle the height of tree
                res.append(level)
        return res
        #have a part for the queue, part for the level and part for checking and add and delete of the queue
        # while deal with the overall queue while for target the level and q is involved with the level so it is in there
             


        
        