class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        n  = len(triangle)
        dp = [[triangle[0][0]]]
        for i in range(1, n):
            m = len(triangle[i])
            max_path = [triangle[i][0] + dp[i-1][0]]
            for j in range(1, m-1):
                max_path.append(min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j])
            
            max_path.append(dp[i-1][m-2] + triangle[i][m-1])

            dp.append(max_path)

            maxt_path = []

        
        return min(dp[n-1])
'''
2 - > [2, ....]
3, 4 -> [5, 6, ...]
6, 5, 7 -> [11, 10, 11]
4, 1, ,8, 3 -> [15, 11, ]
'''