class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #store the complement being target - nums[i]
        store = {}
        for i, val in enumerate(nums):
            compl = target - val
            if compl in store:
                return [store[compl], i]
            store[val] = i
            #you want val to be the key and index to be the value since you are looking up key to find index and returning index
        
            

        