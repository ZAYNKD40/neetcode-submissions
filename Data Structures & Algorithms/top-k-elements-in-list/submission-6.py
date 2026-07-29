class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = 1 + freq.get(i,0)
        array = []
        for i, count in freq.items():
            array.append([count, i])
        array.sort()
        print(array)
        res = []
        while len(res) < k:
            res.append(array.pop()[1])
        return res
        