class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l,r = 0,1
        track = defaultdict(int)
        while r<len(nums):
            print(l,nums[l],r,nums[r])
            if nums[r] in track:
                print('hey')
                l = track[nums[r]]  
                
            if nums[l] == nums[r] and abs(l-r) <=k:
                return True
            elif nums[l] == nums[r]:
                l = r
            track[nums[r]] = r    
            r +=1
            
        return False
        