# https://leetcode.com/problems/valid-anagram/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}

        for c in s:
            if c in map.keys():
                map[c] = map[c] + 1
            else:
                map[c] = 1
        
        for c in t:
            if c in map.keys():
                map[c] = map[c] - 1
                if map[c] < 0:
                    return False
            else:
                return False
        
        for v in map.values():
            if v != 0: return False

        return True