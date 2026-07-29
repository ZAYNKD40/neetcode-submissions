class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #stack,traverse and put into stack
        # when finding first number that beat the last
        # from that number, compute the index difference and put it in the result space for stack
        #pop everything and have that new number in the stack
        
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            #pop everything before if not empty
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
            
        return res
                



        #naive method would be just O(n^2) where for each number you traverse until you find higher date then just write out the condition statements at each steps