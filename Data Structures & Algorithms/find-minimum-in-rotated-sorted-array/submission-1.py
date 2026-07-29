class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l,r = 0, len(nums) - 1 #starting spots

        while l<=r:
            if nums[l] < nums[r]:
                return min(res,nums[l])
            m = (l+r) // 2 #the shrinking window by half, and l and right pointer need to do something 
            res = min(res,nums[m])
            if nums[m] >= nums[l]:
                l = m+1
            else: 
                r = m-1
        return res

        