class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #most brute force way is to go through every number and multiply for each num
        #repeated calculations so do max for each num
        
        maxo = max(nums)
        for i in range(len(nums)-1):
            product = nums[i]
            
            for j in range(i+1,len(nums)):
                 #must be continuous
               
                product *= nums[j]
                
                maxo = max(product, maxo) #save max per i

        return max(maxo, nums[-1])