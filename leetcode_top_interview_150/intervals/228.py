# https://leetcode.com/problems/summary-ranges/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        intervals = []
        if len(nums) == 0:
            return intervals
        
        start = nums[0]
        ant = start
        end = None
        n = len(nums)
        for i in range(1, n):
            if ant == nums[i] - 1:
                end = nums[i]
            else:
                if end != None:
                    intervals.append(str(start) + "->" + str(end))
                    end = None
                else:
                    intervals.append(str(start))
                start = nums[i]
            ant = nums[i]
        
        if end != None:
            intervals.append(str(start) + "->" + str(end))
            end = None
        else:
            intervals.append(str(start))
        
        return intervals