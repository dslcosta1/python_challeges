class Solution:
    def bs(self, nums, ini, end, target):   
        if nums[ini] < target and nums[ini + 1] > target:
            return ini
        
        mid = (ini + end) // 2

        if nums[mid] < target:
            return self.bs(nums, mid, end, target)
        
        return self.bs(nums, ini, mid, target)
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        if n == 0:
            return [-1, -1]
        
        nums.insert(0, -(10**10))
        nums.append(10**10)

        x = self.bs(nums, 0, n+1, target - 0.5)
        if x == -1:
            return [-1, -1]
        x += 1
        if nums[x] != target:
            return [-1, -1]

        y  = self.bs(nums, 0, n+1, target + 0.5)
        if nums[y] != target:
            return [-1, -1]

        return [x-1, y-1]