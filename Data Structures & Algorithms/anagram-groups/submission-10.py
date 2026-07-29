class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create hash map using the sorted letters as the key and the words
        #that use those letters are value belonging to that key
        grouping = defaultdict(list)
        for i in strs:
            sortedLetters = ''.join(sorted(i)) #sort them
            grouping[sortedLetters].append(i) #key and value defined
        return list(grouping.values()) #doing list() since the result we want outputed is list.
        