class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l,r = 0, len(people)-1
        boat = 0
        # a person is considered on the boat when they got r-1 ro l+=1
        while l<=r: #when l == r where is one person left who still need a boat
            if people[l] + people[r] <= limit:
                l +=1
            r-=1 #heavy person always get their own boat, optimized when the light person can get on the heavy person boat
            boat +=1
        return boat


        