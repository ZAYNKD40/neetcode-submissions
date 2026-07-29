class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = {}
        def dp(i):
            if i >= len(nums) :
                return 0
            if i in memo:
                return memo[i]
            memo[i] = nums[i] + max(dp(i+1),0)
            return memo[i]
        for i in range(len(nums)):
            dp(i)
        return max(memo.values())