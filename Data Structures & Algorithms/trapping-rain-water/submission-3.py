class Solution:
    def trap(self, height: List[int]) -> int:
        # base case
        if not height:
                return 0
        l,r = 0, len(height) - 1 #starting point
        leftM, rightM = height[l], height[r] #max update
        res = 0
        # window, window shrink, moving and stopping
        while l<r:
                if leftM < rightM:
                        l +=1
                        leftM = max(leftM, height[l])
                        res += leftM - height[l]
                else:
                        r -=1
                        rightM = max(rightM, height[r])
                        res += rightM - height[r]
        return res
        