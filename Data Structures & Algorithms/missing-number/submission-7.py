class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       #not bit manip approach
       #add everything to what it is suppose to be and compare to sum of nums then subtract for missing
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)
        
       
       
       
       
       
       
       
       
       