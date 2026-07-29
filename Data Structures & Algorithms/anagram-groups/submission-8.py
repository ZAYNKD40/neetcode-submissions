class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for i in strs: #watch the original input, input and output are the main things
            sortedi = ''.join(sorted(i))
            result[sortedi].append(i) #sortedi is key, i is value to be grouped into the keys
        return list(result.values())
        