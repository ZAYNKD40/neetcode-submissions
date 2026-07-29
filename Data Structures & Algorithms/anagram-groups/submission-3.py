class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer= defaultdict(list)
        for i in strs:
            sortedstring = ''.join(sorted(i))
            answer[sortedstring].append(i)
        return list(answer.values())
