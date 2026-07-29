class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #sort, count for current == current + 1 and compare count
        #count scope can be in each loop and each loop end when current!=current+1
        # when it end add it to a list and return max
        nums.sort()
        res =[]
        count = 1
        if len(nums) == 0:
            return 0
        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                count += 1
            elif nums[i] == nums[i+1]:
                continue
            else:
                res.append(count)
                count = 1
        res.append(count)
        return max(res)

