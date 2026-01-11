class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_max = 0
        max_reversed = -inf
        n = len(nums)
        max_sum_reverse = [0] * (n+1)
        max_subsum = [0] * (n+1)

        for i in range(n-1, -1, -1):
            max_subsum[i] = max_subsum[i+1] + nums[i]
            max_reversed = max(max_reversed, max_subsum[i])
            max_sum_reverse[i] = max_reversed
        
        left_curr = 0
        #max_sum = [0] * n
        final_max = -inf
        new_curr_max = 0
        subsum_left = [0]
        for k in range(n):
            left_curr = max(nums[k], nums[k] + left_curr)

            ant_left = subsum_left[-1]

            new_curr_max = max(left_curr,  nums[k]+ant_left+max_sum_reverse[k+1])
            final_max = max(final_max, new_curr_max)
            subsum_left.append(subsum_left[-1] + nums[k])

        return final_max



