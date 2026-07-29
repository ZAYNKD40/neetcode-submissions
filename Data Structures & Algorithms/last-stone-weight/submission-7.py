class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [ -s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            temp = heapq.heappop(stones) - heapq.heappop(stones)
            heapq.heappush(stones, temp)
        return stones[0] * -1 if stones else 0