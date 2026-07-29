class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #need a window size
        import collections
        s = collections.Counter(s1)

        curr = {}
        l = 0
        for r in range(len(s2)):
            curr[s2[r]] = curr.get(s2[r], 0) + 1 #updating current window then compare it to s1 with ds hashmap
            while r - l + 1 > len(s1) and r - l > 0: # window shrinking condition
                curr[s2[l]] -= 1
                if curr[s2[l]] <= 0:
                    del curr[s2[l]]
                l += 1
            #compare
            print(curr, s)
            if curr == s:
                return True
        return False
            


            
            
        