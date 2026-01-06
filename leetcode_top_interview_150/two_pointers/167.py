# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        n = len(numbers)
        i = 0
        j = n - 1

        while i < j:
            if numbers[i] + numbers[j] == target: return [i+1, j+1]

            while numbers[i] + numbers[j] > target:
                j -= 1
            
            while numbers[i] + numbers[j] < target:
                i+= 1
        
        if numbers[i] + numbers[j] == target: return [i, j]
        else: return [0, 0]