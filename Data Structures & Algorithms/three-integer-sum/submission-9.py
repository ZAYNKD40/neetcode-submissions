class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        # res for result and sorting
        #start place and window
        for i, k in enumerate(nums):
            if k > 0: #edge case
                break
            if i > 0 and k == nums[i-1]: #1 out of two duplicate check later check l to prevent duplicate tripplet
                continue
            #starting place that keep changing since we want l in the middle instead of k
            l,r = i+1, len(nums)-1
            while l <r:
                threesum = k + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l +=1
                elif threesum == 0:
                    res.append([k,nums[l], nums[r]])
                    l+=1
                    r-=1
                    #check duplicate for l
                    while nums[l] == nums[l-1] and l<r:
                        l +=1
        return res