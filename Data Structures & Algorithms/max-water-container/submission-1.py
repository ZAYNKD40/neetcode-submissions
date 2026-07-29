class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #calculation, index2-index1, multiply by min between the two index
        #find a starting max, then depend on what is smaller in height at that step
        #move the respective pointer inward until it find something taller then compare again
        #new max replace the old max
        #put the operations of the while loop first and the incrementing condition at the end
        l, r = 0, len(heights) -1
        max = 0
        while l < r:
            vol = (r-l)*min(heights[l],heights[r])
            if vol > max:
                max = vol
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            elif heights[r] == heights[l]: #forgot what if they are equal
                r -=1
        return max
