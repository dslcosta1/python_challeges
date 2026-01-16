# https://leetcode.com/problems/coin-change/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [amount + 1] * (amount + 1)

        dp[0] = 0

        for i in range(1, amount+1):
            for c in coins:
                if c > i:
                    break
                else:
                    dp[i] = min(dp[i], dp[i - c] + 1)

        if dp[-1] > amount:
            return -1

        return dp[-1]
