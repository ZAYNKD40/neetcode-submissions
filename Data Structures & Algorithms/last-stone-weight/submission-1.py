class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        

        while len(stones) > 1:
            if stones[-1] == stones[-2]:
                del stones[-2:]
            elif stones[-1] != stones[-2]:
                temp = stones[-1] - stones[-2]
                del stones[-2:]
                stones.append(temp)
                stones.sort()
                print(stones)
        if stones:
            res = stones[0]
            return res
        else:
            return 0
        