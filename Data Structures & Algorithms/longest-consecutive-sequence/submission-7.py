class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nodup = set(nums)
        countf=0
        for n in nums:
            count = 1
            if (n - 1) not in nodup:
                while (n + count) in nodup:
                    count += 1
            countf = max(count,countf)
        return countf