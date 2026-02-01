class Solution:


    def bfs(self, line, target, ini, end):
        
        if ini >= end:
            return -1
        if ini <=target and ini == len(line) -1:
            return ini
        if line[ini] <= target and line[ini+1] > target:
            return ini

        mid = (ini + end) // 2

        if target >= line[mid]:
            return self.bfs(line, target, mid, end)
        else:
            return self.bfs(line, target, ini, mid)
        

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])


        first_line = []
        for j in range(n):
            first_line.append(matrix[j][0])

        first_line.append(10**6)
        print(first_line)
        index_i = self.bfs(first_line, target, 0, n)
        #print("index_i: ", index_i)
        if index_i == -1:
            return False

        col = matrix[index_i]
        col.append(10**6)
        index_j = self.bfs(col, target, 0, m)
        #print("index_j: ", index_j)
        if index_j == -1:
            return False

        
        return matrix[index_i][index_j] == target
