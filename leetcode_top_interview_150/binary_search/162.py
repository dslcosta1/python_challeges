# https://leetcode.com/problems/find-peak-element/?envType=study-plan-v2&envId=top-interview-150

class Solution:

    def searchPeak(self, nums, ini, end):
        if ini > end: return None

        mid =  (ini + end) //2
        if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
            return mid -1
        
        if nums[mid] <= nums[mid + 1]:
            return self.searchPeak(nums, mid+1, end)
        else:
            return self.searchPeak(nums, ini, mid)

    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        nums = [-inf] + nums + [-inf]
        
        return self.searchPeak(nums, 1, len(nums) -2)