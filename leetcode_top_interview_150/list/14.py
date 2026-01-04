# https://leetcode.com/problems/longest-common-prefix/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        n = len(strs)
        for i in range(1, n):
            s = strs[i]
            max_len = min(len(s), len(prefix))
            s = s[:max_len]
            prefix = prefix[:max_len]
            while s != prefix:
                s = s[:-1]
                prefix = prefix[:-1]
                if len(prefix) == 0: return ""

        return prefix            

