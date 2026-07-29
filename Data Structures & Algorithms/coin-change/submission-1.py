class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(amount):
            #base case
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            res = 1e9
            for coin in coins:
                if amount - coin >=0: #if valid and can be chosen
                    res = min(res, 1+dp(amount - coin) ) #reducing the amount and go back down and also save and use these computations
            memo[amount] = res
            return res

        mincoin = dp(amount) #use your function
        return -1 if mincoin >= 1e9 else mincoin







        #solving using dp and memoize
        #given list of coins and a target amount, return least amount of coin needed, a count not a list
       
