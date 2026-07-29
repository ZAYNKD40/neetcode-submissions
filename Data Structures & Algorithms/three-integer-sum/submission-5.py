class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i, k in enumerate(nums):
            if k > 0:
                break
            if i>0 and k == nums[i-1]:
                continue
            l,r = i+1, len(nums)-1
            while l<r:
                combine = k+ nums[l]+ nums[r]
                if combine == 0:
                    res.append([k,nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                    while l<r and nums[r] == nums[r+1]:
                        r -= 1
                elif combine > 0:
                    r -= 1
                elif combine < 0:
                    l += 1
        return res