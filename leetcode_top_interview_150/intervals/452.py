class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        arrow = 0
        points.sort()
        points.append([10**18, 10**18])

        ballon = points.pop(0)
        x = ballon[1]
        while len(points) > 0:

            ballon = points.pop(0)
            while x >= ballon[0] and len(points) != 0:
                x = min(x, ballon[1])
                ballon = points.pop(0)
                
            
            arrow += 1
            x = ballon[1]

        return arrow
