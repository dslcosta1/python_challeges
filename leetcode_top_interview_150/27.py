# https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        pointer_1 = 0
        pointer_2 = 0

        size = len(nums)

        while pointer_2 < size:
            if nums[pointer_2] != val:
                nums[pointer_1] = nums[pointer_2]
                pointer_1 += 1

            pointer_2 += 1

        return pointer_1