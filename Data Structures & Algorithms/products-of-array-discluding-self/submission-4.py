class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            total = 1
            # Multiply all elements after i
            for j in range(i+1, len(nums)):
                total *= nums[j]
            # Multiply all elements before i
            for z in range(i-1, -1, -1):
                total *= nums[z]
            res.append(total)
        return res

        