# https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150

class Solution:

    def reverse(self, nums, ini, end) -> None:

        while ini < end:
            aux = nums[end]
            nums[end] = nums[ini]
            nums[ini] = aux
            ini += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        if k > n:
            k = k % n
        
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)