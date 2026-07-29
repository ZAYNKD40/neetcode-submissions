class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: #edge case
            return 0
        # starting at both end, go inward
        l, r = 0, len(height) - 1
        # the current leftM and rightM are already defined, that is why updating pointer then max work
        leftMax, rightMax = height[l], height[r]
        res = 0 #extracting info from operations
        # window, window shrinking, movement and movement stop
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l] #current water at exact x axis
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r] #current water at exact x axis
        return res