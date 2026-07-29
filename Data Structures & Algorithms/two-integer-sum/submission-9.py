class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        #storing
        for i, val in enumerate(nums):
            store[val] = i
        for i, val in enumerate(nums):
            diff = target - val
            if diff in store and store[diff] != i:
                return [i, store[diff]]

        