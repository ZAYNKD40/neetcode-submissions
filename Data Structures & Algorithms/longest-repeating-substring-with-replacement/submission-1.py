class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # two pointers are about shrinking the window as you go
        # need the conditions or guardrail to do it and ignore prior, storing info
        # of the prior then move on
        # r-l+1 is the left window size
        count = defaultdict(int)
        maxf = 0
        l = 0
        res = 0
        for r in range(len(s)):
            count[s[r]] += 1
            maxf = max(count[s[r]], maxf) #used to track the most dominant character
            while (r - l + 1) - maxf > k: # when size of window - most dominant char is larger than k buffer
                count[s[l]] -= 1 # update the window, size plus the count within the window
                l+=1
            res = max(res, r-l+1) # if guardrail isnt reached then the result is not the highest frequency window but window size + 1 since first number is also counted 

        return res
