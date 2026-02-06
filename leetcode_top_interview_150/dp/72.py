class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

    # Compose the string
        n = len(word1)
        m = len(word2)

        dp = []
        for i in range(n+1):
            dp.append([0] * (m+1))
                
        for i in range(n+1):
            for j in range(m+1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:
                    if word1[i-1] == word2[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        replace = dp[i-1][j-1]
                        delete = dp[i][j-1]
                        insert = dp[i-1][j]
                        dp[i][j] = min(replace, delete, insert) + 1

        return dp[n][m]