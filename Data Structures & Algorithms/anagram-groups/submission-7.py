class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for i in strs:
            sorteds =''.join(sorted(i)) #creating the keys to group the values together so determine that sorteds is key
            if sorteds not in group:
                group[sorteds]= []
            group[sorteds].append(i) 
        return list(group.values())
