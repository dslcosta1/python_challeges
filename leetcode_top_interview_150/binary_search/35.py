# https://leetcode.com/problems/search-insert-position/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def binarySearch(self, nums, target, start, end):
        if start >= end or start >= len(nums):
            if target <= nums[start]: return start
            if target > nums[start]: return start + 1
        
        if nums[start] < target and nums[start + 1] >= target:
            return start + 1

        mid = (start + end)//2

        if target == nums[mid]: return mid

        if target < nums[mid]: return self.binarySearch(nums, target, start, mid)

        return self.binarySearch(nums, target, mid+1, end)

    
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        return self.binarySearch(nums, target, 0, n-1)