class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l<=r:
            print(l,r)
            m = (r+l) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
                if l > r:
                    return l
            elif nums[m] > target:
                r = m - 1
                if r < l and not r<0:
                    return l
                elif r<l and r<0:
                    return 0
            
        