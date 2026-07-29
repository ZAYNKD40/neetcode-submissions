class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def robtool(nums):
            rob1,rob2 = 0,0
            for n in nums:
                rob1,rob2 = rob2, max(rob2, n+rob1)
            return rob2
        return max(robtool(nums[:-1]), robtool(nums[1:])) #if array have 1 element it will return empty list in python splice instead of an error