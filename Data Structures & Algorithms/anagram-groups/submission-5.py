class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for i in strs:
            sorteds =''.join(sorted(i)) #creating the keys to group the values together
            group[sorteds].append(i) 
        return list(group.values())
