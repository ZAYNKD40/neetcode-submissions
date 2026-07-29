class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #stack,traverse and put into stack
        # when finding first number that beat the last
        # from that number, compute the index difference and put it in the result space for stack
        #pop everything and have that new number in the stack
        
        res = []
        for i in range(len(temperatures)):
            if i == len(temperatures) - 1:
                res.append(0)
                break
            j = i+1
            while j < len(temperatures):
                if temperatures[j] > temperatures[i]:
                    res.append(j - i)
                    break
                elif temperatures[j] <= temperatures[i]:
                    j += 1
                if j == len(temperatures) and temperatures[j -1] <= temperatures[i]:
                    res.append(0)
                    break

        return res
                



        #naive method would be just O(n^2) where for each number you traverse until you find higher date