class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #basic of two pointers
        # need incrementing and stopping condition
        # need window left right and guard rail for window update
        #  need information record
        #method utilized will be determining dominant characters and returning relevant windowsize that does not surpass buffer k
        maxfreq = 0
        l = 0
        res = 0
        count = {}
        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0) + 1
            maxfreq = max(maxfreq, count[s[r]])
            while r - l +1 - maxfreq > k: #when the left window minority is larger than k, using while so when new thing added from r change from minority to dominant it would update accordingly
                count[s[l]] -= 1
                l +=1
            res = max(res, r-l+1) #because we built a good window already it can be used here
        return res
        