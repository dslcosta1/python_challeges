class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        prod = 1
        count_zeros = 0
        index_zero = 0
        for i in range(n):
            if nums[i] != 0:
                prod *= nums[i]
            else:
                count_zeros += 1
                index_zero = i
        
        if count_zeros > 1:
            return [0] * n
        
        if count_zeros == 1:
            re = [0] * n
            re[index_zero] = prod
            return re

        result = []
        for i in range(n):
            result.append(prod//nums[i])
        
        return result