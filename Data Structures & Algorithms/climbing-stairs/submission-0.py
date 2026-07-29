class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1,1 # have 2 variables
        # loop through n- 1 times, add and shift back upward
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one
        # this is solving the problem from the bottom of dfs upward
        

        

        