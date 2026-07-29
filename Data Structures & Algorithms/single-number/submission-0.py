class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            print("input:"+ str(n) + ' ' + str(res))
            res = n ^ res
        return res

        