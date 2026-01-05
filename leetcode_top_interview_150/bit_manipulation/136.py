# https://leetcode.com/problems/single-number/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        result = nums[0]
        n = len(nums)
        for i in range(1, n):
            result = result^nums[i]

        
        return result