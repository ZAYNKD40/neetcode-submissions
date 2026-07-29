class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create hash map using the sorted letters as the key and the words
        #that use those letters are value belonging to that key
        grouping = defaultdict(list)
        for i in strs:
            sortedLetters = ''.join(sorted(i))
            grouping[sortedLetters].append(i)
        return list(grouping.values())
        