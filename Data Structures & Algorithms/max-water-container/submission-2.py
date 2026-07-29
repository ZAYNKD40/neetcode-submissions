class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #max is min(l,r)*(rpos-lpos)
        maxa = 0
        l,r = 0, len(heights) - 1
        while l<r:
            #recorder
            maxa = max(maxa,min(heights[l],heights[r]) * (r-l))
            #incrementer
            #only way for the inside to be larger than outside is if a heihgt is higher
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return maxa

        