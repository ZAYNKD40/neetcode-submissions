class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(list)
        freq = [[] for i in range(len(nums)+1)]
        #num is key

        for num in nums:
            count[num]= 1+ count.get(num,0)
        for num, cnt in count.items():
            freq[cnt].append(num)
            
        res =[]
        for i in range(len(freq)-1,-1,-1):
            for num in freq[i]:
                if len(res) < k:
                    res.append(num)
        return res
           
