class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # window def and shrinking mechanism
        # movement and starting point
        # information carrier
        # while sum >= target, shrink left, if sum - left < target in while loop break
        # movement is left and right pointer, right to iterate, left to shrink using while loop
        # information extract min len that still fit the while condition and before the break loop
        l=0
        #just need min window, no need to store window and use sum() since it is O(n) and terrible space
        # just use a curr sum variable and if window shrink subtract left pointer
        currsum = 0 #a carry-on sum
        sub = len(nums)
        if sum(nums) < target: #base case/ edge case
            return 0
        elif sum(nums) == target:
            return len(nums)
        for r in range(len(nums)):
            currsum += nums[r]
            while currsum >= target:
                if currsum - nums[l] < target:
                    sub = min(sub, r-l+1)
                    break
                currsum -= nums[l]
                l +=1
        return sub
            

        