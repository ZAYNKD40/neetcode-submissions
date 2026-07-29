class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        storeFreq = {}
        for num in nums:
            storeFreq[num] = 1 + storeFreq.get(num, 0)
        arr = []
        for num, cnt in storeFreq.items(): #iterating through freqencies need one of three . methods
            arr.append([cnt, num])  #missed [] 
        arr.sort()
        result = []
        while len(result) < k: 
            result.append(arr.pop()[1])
        return result

#hastags are for wrongs and reason of mistake.
        