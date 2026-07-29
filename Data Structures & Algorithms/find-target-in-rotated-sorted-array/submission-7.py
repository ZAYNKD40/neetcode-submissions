class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            # left half is sorted
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:  # target in left half
                    r = m - 1
                else:                             # target in right half
                    l = m + 1

            # right half is sorted
            else:
                if nums[m] < target <= nums[r]:  # target in right half
                    l = m + 1
                else:                             # target in left half
                    r = m - 1

        return -1