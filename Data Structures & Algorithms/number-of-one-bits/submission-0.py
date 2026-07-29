class Solution:
    def hammingWeight(self, n: int) -> int:
    
        c = bin(n)[2:]
        count = 0
        for i in c:
            if i == "1":
                count += 1
        return count

        