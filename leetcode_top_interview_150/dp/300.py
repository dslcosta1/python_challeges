class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        max_count = 1
        increases = [1] * n
        

        for i in range(n, -1, -1):

            for j in range(i, n, 1):
                if nums[j] > nums[i]:
                    increases[i] = max(increases[j] + 1, increases[i])
                    max_count = max(max_count, increases[i])

        return  max_count