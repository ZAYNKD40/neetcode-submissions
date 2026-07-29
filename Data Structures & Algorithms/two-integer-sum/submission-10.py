class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {val: i for i,val in enumerate(nums)}

        for i, val in enumerate(nums):
            diff = target - val
            if diff in store and i!= store[diff]:
                return [i, store[diff]]
        