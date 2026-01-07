# https://leetcode.com/problems/merge-intervals/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        vi = [0] * 10002
        ve = [0] * 10002
        minv = 10002
        maxv =  -1
        for i in intervals:
            vi[i[0]] += 1
            ve[i[1]] += -1

            maxv = max(maxv, i[1])
            minv = min(minv, i[0])

        s = 0
        start = -1
        new_interval = []
        for j in range(minv, maxv+1):
            s += vi[j]
            
            if start == -1 and vi[j] > 0:
                start = j

            s += ve[j]

            if s == 0 and ve[j] < 0:
                new_interval.append([start, j])
                start = -1
        
        return new_interval