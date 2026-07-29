class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort approach. need count dictionary still
        # Then use array of lists to store in appropriate index according to frequency
        # then append from the last list backward in result according to how many k needed
        # start, stop, increment so len(res)-1, 0, -1 start at the end
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        freq = [[] for i in range(len(nums) + 1)] #need bucket from 0 to length of num since index work from 0 even if you don't need the 0 bucket
        for num, cnt in count.items():
            freq[cnt].append(num) #freq[cnt] because it is an index
        res = []
        for i in range (len(freq)-1, 0, -1):
            for num in freq[i]: #if it is for num in freq here num would be the bucket instead of the numbers in the buckets.
                res.append(num)
            if len(res) == k:
                return res
        
        