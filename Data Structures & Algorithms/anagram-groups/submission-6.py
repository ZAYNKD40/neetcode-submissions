class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for i in strs:
            sorteds =''.join(sorted(i)) #creating the keys to group the values together
            if sorteds not in group:
                group[sorteds]= []
            group[sorteds].append(i) 
        return list(group.values())
