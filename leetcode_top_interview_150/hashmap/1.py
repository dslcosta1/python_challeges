class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        n = len(nums)
        for i in range(n):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap[diff], i]
            
            hashmap[nums[i]] = i
        
        return [-1, -1]