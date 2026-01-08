# https://leetcode.com/problems/combinations/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    result = []

    def backtracking(self, ini, end, k, nums):
        print(nums)
        if len(nums) == k: 
            self.result.append(nums[:])
            return

        if len(nums) + (end - ini) < k:
            return
        
        for i in range(ini, end):
            nums.append(i)
            self.backtracking(i+1, end, k, nums)

            nums.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.result = []
        self.backtracking(1, n+1, k, [])

        return self.result