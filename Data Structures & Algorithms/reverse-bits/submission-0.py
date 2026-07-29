class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:] #strip the 0b when counting, matter when counting 0 since bin give 0b......
        padding = binary.zfill(32)
        res = padding[::-1]
        return int(res,2)
        