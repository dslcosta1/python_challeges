class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[0] * m for _ in range(n)]
        
        if  obstacleGrid[0][0] == 1:
            return 0
        
        def pathToStar(i, j):
            if i == n-1 and j == m-1:
                if obstacleGrid[i][j] != 0:
                    return 0
                else:
                    return 1

            if dp[i][j] != 0:
                return dp[i][j]
            
            paths = 0
            if i + 1 < n and obstacleGrid[i+1][j] != 1:
                l = pathToStar(i+1, j)
                paths += l
        
            if j + 1 < m and obstacleGrid[i][j+1] != 1:
                l = pathToStar(i, j+1)
                paths += l

            dp[i][j] = paths
            return paths
        
        return pathToStar(0, 0)
