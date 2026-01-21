# https://leetcode.com/problems/insert-interval/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        final = []
        x = -1
        y = -1
        newIntervalWasIncluded = False
        for interval in intervals:
            if interval[0] < newInterval[0] and interval[1] < newInterval[0]:
                final.append(interval)
            
            if interval[0] > newInterval[1] and interval[1] > newInterval[1]:
                if newIntervalWasIncluded == False:
                    if x != -1 and y != -1:
                        final.append([x, y])
                    else:
                        final.append(newInterval)
                newIntervalWasIncluded = True
                x, y = -1, -1
                final.append(interval)
            
            if interval[0] <= newInterval[0] and interval[1] >= newInterval[0]:
                x = interval[0]
                y = max(newInterval[1], interval[1])

            if interval[0] > newInterval[0] and  interval[0] <= newInterval[1]:
                if x == -1:
                    x = newInterval[0]
                
                y = max(interval[1], newInterval[1])

        if newIntervalWasIncluded == False:
            if x != -1 and y != -1:
                final.append([x, y])
            else:
                final.append(newInterval)
        
        return final
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        final = []
        x = -1
        y = -1
        newIntervalWasIncluded = False
        for interval in intervals:
            if interval[0] < newInterval[0] and interval[1] < newInterval[0]:
                final.append(interval)
            
            if interval[0] > newInterval[1] and interval[1] > newInterval[1]:
                if newIntervalWasIncluded == False:
                    if x != -1 and y != -1:
                        final.append([x, y])
                    else:
                        final.append(newInterval)
                newIntervalWasIncluded = True
                x, y = -1, -1
                final.append(interval)
            
            if interval[0] <= newInterval[0] and interval[1] >= newInterval[0]:
                x = interval[0]
                y = max(newInterval[1], interval[1])

            if interval[0] > newInterval[0] and  interval[0] <= newInterval[1]:
                if x == -1:
                    x = newInterval[0]
                
                y = max(interval[1], newInterval[1])

        if newIntervalWasIncluded == False:
            if x != -1 and y != -1:
                final.append([x, y])
            else:
                final.append(newInterval)
        
        return final
