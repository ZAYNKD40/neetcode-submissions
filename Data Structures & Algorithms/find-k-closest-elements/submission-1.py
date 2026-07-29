class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #sliding window approach
        #l at 0 r at the end, then go inward while the length is still more than k
        # comparing distance using absolute value and difference, move right move left as conditioned
        l,r = 0, len(arr) -1
        while r-l + 1 > k:
            if abs(x-arr[l]) <= abs(x-arr[r]): #if the right is farther
                r -=1
            else:
                l+=1


        return arr[l:r+1]