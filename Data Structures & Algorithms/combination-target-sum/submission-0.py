class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        #using dfs, backtracking
        res = []

        def dfs(i,cur,total):
            #writing base case for recursion
            if total == target:
                res.append(cur.copy()) #appending the cur
                return #terminate when equal
            if i >= len(nums) or total > target: #second base case stopping when overshoot
                return
            cur.append(nums[i]) #using i as pointer for traversal within dfs recursion
            dfs(i,cur,total+nums[i])
            cur.pop()
            dfs(i+1,cur,total)


        #calling the dfs function built
        dfs(0,[],0)
        return res