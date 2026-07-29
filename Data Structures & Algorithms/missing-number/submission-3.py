class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       #not bit manip approach
       #create a set to look up n+1 and n-1 then return
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
        
       
       
       
       
       
       
       
       
       