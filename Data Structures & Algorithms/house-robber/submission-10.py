class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1,rob2 = 0,0
        for n in nums:
            rob1,rob2 = rob2,max(rob2, n+rob1)
        return rob2
        #rob2 is current best, n for new calculations

        '''
        
- `rob1` = best you can rob **2 houses behind**
- `rob2` = best you can rob **1 house behind** (current best)
- For each new house `n`, you choose:
  - **Skip it** → keep `rob2`
  - **Rob it** → `n + rob1` (can't use adjacent, so jump back 2)

        '''
        