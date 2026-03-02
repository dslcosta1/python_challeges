from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hm = defaultdict(int)
        
        for n in nums:
            hm[n] += 1

            if hm[n] >= len(nums)/2:
                return n
        
        return 0 
