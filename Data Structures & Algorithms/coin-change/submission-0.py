class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        #store computed paths

        #creating dfs
        def dfs(amount): #try all the different ways to reach amount
            if amount == 0:
                return 0
            if amount in memo: #the dp, a bigger amount constitute many smaller amounts and those are computed before
                return memo[amount]
            res = float('inf')
            for coin in coins:
                if amount - coin >= 0: #if amount can never be at 0 but keep overshooting
                    res = min(res, 1+ dfs(amount - coin))
            #store in memo
            memo[amount] = res
            return res
        mincoin= dfs(amount)
        return -1 if mincoin >= float('inf') else mincoin



        