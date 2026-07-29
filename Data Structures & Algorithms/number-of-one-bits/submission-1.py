class Solution:
    def hammingWeight(self, n: int) -> int:
        # learn the bin (binary) function and the .count() function, count is counting the binary using C so it is quciker
        return bin(n).count('1')