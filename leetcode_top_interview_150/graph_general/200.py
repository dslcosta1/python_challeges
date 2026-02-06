class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        island_count = 0

        for i in range(m):
            for j in range(n):
                queue = []
                if grid[i][j] == '1':
                    queue.append((i, j))
                    island_count += 1

                while queue:
                    x, y = queue.pop(0)

                    if grid[x][y] == '1':
                        if x-1 >= 0 and grid[x-1][y] == '1':
                            queue.append((x-1, y))
                        
                        if y-1 >= 0 and grid[x][y-1] == '1':
                            queue.append((x, y-1))

                        if x+1 < m and grid[x+1][y] == '1':
                            queue.append((x+1, y))
                        
                        if y+1<n and grid[x][y+1] == '1':
                            queue.append((x, y+1))

                    grid[x][y] = '#'
        
        return island_count