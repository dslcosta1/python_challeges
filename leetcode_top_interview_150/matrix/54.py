# https://leetcode.com/problems/spiral-matrix/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        result = []

        n = len(matrix)
        if n <= 0:
            return result
        m = len(matrix[0])

        x = 0
        y = 0
        j = 0
        signal_x = 1
        signal_y = 0
        gap = 0
        s = 1
        for i in range(m*n):
            result.append(matrix[x][y])

            if (x==gap and y==gap-1 and j%4==3) or (x==gap and y==m-1-gap and j%4==0) or (x==n-1-gap and y==m-1-gap and j%4==1) or (x==n-1-gap and y ==gap and j%4==2):
                j += 1
                if j%2 == 0:
                    s = s*-1

                signal_x = s*((signal_x + 1) % 2)
                signal_y = s*((signal_y +1) % 2)

                if j%4 == 3:
                    gap +=1


            x += signal_y
            y += signal_x
    

        return result
