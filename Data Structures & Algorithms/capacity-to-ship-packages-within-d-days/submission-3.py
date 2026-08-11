class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #create binary search on a number string weight capacity different from the weights
        #list. with least being max weight, and max being sum of all weight so all in one day
        # l, r = max(weights), sum(weights). m = (l+r)//2
        # incrementing, if need to carry faster to reach day, then l+, if need slower, then r+
        l,r = max(weights), sum(weights)
        res = r
        while l <= r:
            #binary search
            m = (l+r)//2
            #comparison against
            
            tday = 0
            tempm = m
            counter = 0 # could use otjher methods, but this is for counting last container
            for i in weights:
                tempm -= i
                counter+=1
                if tempm <0:
                    tempm = m-i #packing them into days, if less than zero go to the next day by reseting
                    tday +=1
                    print("yes1")
                if tempm == 0:
                    tempm = m
                    tday+=1
                    print("yes2")
                elif counter == len(weights) and tempm > 0:
                    tday+=1
                    print("yes3")
            print(m,tday)
            if tday > days:
                l = m+1
                
            if tday <= days:
                res = m
                r = m - 1
        return res
        
        
        