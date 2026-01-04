# https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        i = 0
        j = 0
        while j < m and i < n:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        
        return i == n
             