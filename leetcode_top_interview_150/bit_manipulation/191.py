# https://leetcode.com/problems/number-of-1-bits/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        binary = bin(n)[2:]
        count = 0
        for b in binary:
            if b == '1':
                count += 1

        return count
