class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * (len(nums)+1)
        def dp(i):
            if i >= len(nums): #standard base case
                return 0
            if memo[i] != -1: # standard base case for the dp, prevent recompute
                return memo[i]
            memo[i] = nums[i] + max(dp(i+2), dp(i+3)) #actual arhitectural decision + recursion
            return memo[i] #return the calculation to the recursion
        return max(dp(0),dp(1))
        # the logic is, the best decision at any position is to get the max at the +2 or skip the +2 position entirely and go +3
        # top down, after the way is defined, the future calculation will go to base case and give the answer backward.