# https://leetcode.com/problems/jump-game/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        goal = n

        for i in range(n-1, -1, -1):
            if nums[i] + i >= goal:
                goal = i

        if goal == 0: return True
        else: return False