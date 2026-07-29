class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp, storing the past calculated results and using it for future calculations
        rob1,rob2 = 0, 0
        for n in nums: #up to current elem max
            rob1, rob2 = rob2, max(rob2, n+rob1)
        return rob2
        