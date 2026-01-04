# https://leetcode.com/problems/sqrtx/?envType=study-plan-v2&envId=top-interview-150

class Solution:

    def binarySearch(self, x, start, end):
        middle = floor((start + end)/2)
        middle_square = middle * middle
        next_middle_square = (middle+1) * (middle+1)
        
        if middle_square <= x and next_middle_square > x:
            return middle
        elif middle_square <= x:
            return self.binarySearch(x, middle+1, end)
        else:
            return self.binarySearch(x, start, middle)

    def mySqrt(self, x: int) -> int:
        return self.binarySearch(x, 0, x)