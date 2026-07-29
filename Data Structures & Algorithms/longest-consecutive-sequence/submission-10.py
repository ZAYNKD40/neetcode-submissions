class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nodup = set(nums)
        countf=0
        for n in nums:
            if (n - 1) not in nodup: #only run when needed aka on sequence starter
                count = 1
                while (n + count) in nodup:
                    count += 1
                countf = max(count,countf)
        return countf