class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #have first level forloop, in it have if loop to check if k > 0, if it is there is no way to make a zero
        #have it go k,l,r and handle double by if k == last k then continue, for l and r increment them
        #inside the forloop r and l will be reset each time and l will be next to k so index of k +1
        #while loop 4 checks, go left, go right and doubles for l and r
        res = []
        nums.sort()
        
        for i, k in enumerate(nums):
            if k > 0:
                break
            
            # Fix: Check i > 0 first
            if i > 0 and k == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            
            # Fix: while l < r (not l < k)
            while l < r:
                # Fix: Calculate sum inside the loop
                combine = k + nums[l] + nums[r]
                
                if combine == 0:
                    res.append([k, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Fix: Skip duplicates AFTER finding a valid triplet
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif combine < 0:
                    l += 1
                else:  # combine > 0
                    r -= 1
                    
        return res