class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)
        for i in strs:
            sorte = ''.join(sorted(i))
            ana[sorte].append(i)
        return list(ana.values())