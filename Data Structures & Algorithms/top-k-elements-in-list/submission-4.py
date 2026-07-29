class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}
        for i in nums:
            store[i] = 1 + store.get(i,0)
        arr = []
        for i, count in store.items():
            arr.append([count,i])
        arr.sort()
        res = []
        while len(res)<k:
            res.append(arr.pop()[1])
        return res
        