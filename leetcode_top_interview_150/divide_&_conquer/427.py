'''
class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
'''

class Solution:    
    
    def construct(self, grid: List[List[int]]) -> 'Node':
        total_sum = 0
        n = len(grid)
        if n == 0: return None
            
        for line in grid:
            total_sum += sum(line)
        print(total_sum)
        
        if total_sum == 0 or total_sum == n * n:
            return Node(grid[0][0] == 1, True)
        
        nodes = Node(True, False)

        topLeftGrid = []
        
        for i in range(n//2):
            topLeftGrid.append(grid[i][:n//2])
        nodes.topLeft = self.construct(topLeftGrid)

        topRightGrid = []
        for i in range(n//2):
            topRightGrid.append(grid[i][n//2:])
        nodes.topRight = self.construct(topRightGrid)

        bottonLeftGrid = []
        for i in range(n//2, n):
            bottonLeftGrid.append(grid[i][:n//2])
        nodes.bottomLeft = self.construct(bottonLeftGrid)


        bottonRightGrid = []
        for i in range(n//2, n):
            bottonRightGrid.append(grid[i][n//2:])
        nodes.bottomRight = self.construct(bottonRightGrid)

        return nodes
        
        