class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1): #exclusive not inclusive
            res.append(bin(i).count('1'))
        return res
        #this is O(nlogn) because for loop is O(n) and for each you are doing .count which is logn