# https://leetcode.com/problems/group-anagrams/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}

        for s in strs:
            chars_sorted = sorted(s)
            s_sorted = "".join(chars_sorted)
            if s_sorted in hashmap:
                hashmap[s_sorted].append(s)
            else:
                hashmap[s_sorted] = [s]
        
        strs_outuput = []
        for k in hashmap.keys():
            strs_outuput.append(hashmap[k])

        return strs_outuput
        