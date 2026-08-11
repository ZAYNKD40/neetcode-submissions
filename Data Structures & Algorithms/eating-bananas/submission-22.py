class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        res = r

        # while loop to binary search m (lowest to highest rate)
        while l <= r:
            m = (l+r) // 2
            # condition to check against
            tot = 0
            for i in piles:
                tot += math.ceil(float(i/m))
            
            # incrementing condition
            if tot <= h: # high number on numberline, need to find max
                res = min(res,m)
                r = m -1
                
            if tot > h: # number too low on number line
                l = m + 1
            
        return res
#it tot < h, then eating rate is quick, keep searching for min, if tot>h, not answer at all
            