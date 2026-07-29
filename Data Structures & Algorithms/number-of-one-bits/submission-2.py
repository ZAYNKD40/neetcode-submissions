class Solution:
    def hammingWeight(self, n: int) -> int:
        # just shift to the right by 1 each time
        # before shift, add the mod by 2 since it is binary it will either return 0 or 1
        res = 0
        while n:
            res += n % 2
            n = n >> 1
        return res
        