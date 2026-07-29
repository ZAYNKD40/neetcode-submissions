class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    # a list of strings turned into one string with their length captured and also act as separator
    # the structure of the information is length#actualString
    # this is two separate methods, they are not calling each other
    # this decoding is using i to traverse entire and using j index of anchor for where string start
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1 #j go to # and find start of first string
            length = int(s[i:j]) # decoding the length info stored
            i = j + 1 # jump to start of length extracted string
            j = i + length
            res.append(s[i:j]) #append the word from i to j and put it as an elem in a list
            i = j #set i to the end of the string and for j to find the next # again in the next iteration of while loop
        return res

