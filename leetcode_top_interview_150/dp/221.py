# https://leetcode.com/problems/maximal-square/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])

        dp = []
        for i in range(m):
            dp1 = []
            for j in range(n):
                dp1.append(0)
            dp.append(dp1)
        max_area = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    d = 0
                    if i -1 < 0 or j-1 < 0:
                        d = 1
                    else:
                        d = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    
                    if d > 0:
                        max_area = max(max_area, d*d)
                    
                    dp[i][j] = d
        return max_area