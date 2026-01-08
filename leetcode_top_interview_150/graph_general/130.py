# https://leetcode.com/problems/surrounded-regions/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        m = len(board)
        n = len(board[0])
        visited = [b[:] for b in board]
        group = []
        stack = []
        hasEdge = False

        for i in range(1, m-1):
            for j in range(1, n-1):
                if visited[i][j] == 'O':
                    stack.append([i, j])
                    visited[i][j] = '#'
                    
                while len(stack) > 0:
                    x, y = stack.pop()
                    group.append([x, y])

                    for p in [(0,1),(0,-1),(1,0),(-1,0)]:
                        k, l = p
                        if  x+k >= 0 and x+k <= m -1 and y+l >= 0 and y+l <= n-1:
                            if visited[x+k][y+l] == 'O':
                                if x+k == 0 or x+k == m -1 or y+l == 0 or y+l == n-1:
                                    hasEdge = True
                                else:
                                    stack.append([x+k, y+l])
                                visited[x+k][y+l] = '#'      
                if not hasEdge:
                    for g in group:
                        board[g[0]][g[1]] = 'X'
                
                hasEdge = False
                group = []
        
        return board