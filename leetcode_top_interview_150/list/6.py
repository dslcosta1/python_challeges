# https://leetcode.com/problems/zigzag-conversion/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        m = (numRows - 1)
        substring = [''] * numRows
        if m <= 0: return s
        
        for i in range(n):
            pos = i % m

            dir = i // m

            if dir % 2 == 0:
                substring[pos] = substring[pos] + s[i]
            else:
                j = m - pos
                substring[j] = substring[j] + s[i]
        
        result = ""
        for sub in substring:
            result += sub

        return result