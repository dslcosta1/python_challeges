class Solution:


    max_values = []

    def maxSub(self, nums:List[int], curr):
        if curr == len(nums) -1:
            self.max_values.append(nums[curr])
            return nums[curr]
        
        max_sum = self.maxSub(nums, curr+1)

        if max_sum <= nums[curr] + self.max_values[-1] or max_sum < nums[curr]:
            if max_sum < nums[curr] + self.max_values[-1]:
                max_sum = nums[curr] + self.max_values[-1]
            
            if max_sum < nums[curr]:
                max_sum = nums[curr] 

            self.max_values.append(max_sum)
        else:
            self.max_values.append(max(self.max_values[-1] + nums[curr],nums[curr]))

        return max_sum

    def maxSubArray(self, nums: List[int]) -> int:
        # if len(nums) == 1: return nums[0]
        return self.maxSub(nums, 0)


[5, 4, -1, 7, 8, -2, -20]
