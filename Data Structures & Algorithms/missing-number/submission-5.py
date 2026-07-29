class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       #not bit manip approach
       #add everything to what it is suppose to be and compare to sum of nums then subtract for missing
        sumn = sum(nums)
        def addall(n):
            res = 0
            for i in range(n+1):
                res+= i
            return res
                


        if sumn == addall(len(nums)):
            return 0
        else:
            return (addall(len(nums)) - sumn)
        
       
       
       
       
       
       
       
       
       