class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            setc = set()
            for j in range(i,len(s)):
                if s[j] in setc:
                    break
                else:
                    setc.add(s[j])
            res = max(res, len(setc))
        return res

        