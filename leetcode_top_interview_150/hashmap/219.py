# https://leetcode.com/problems/contains-duplicate-ii/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        n = len(nums)
        for i in range(n):
            if i <= k:
                if nums[i] in hashmap: return True
                hashmap[nums[i]] = True
            else:
                first  = nums[i - k - 1]
                del hashmap[first]

                if nums[i] in hashmap: return True
                hashmap[nums[i]] = True

        return False 