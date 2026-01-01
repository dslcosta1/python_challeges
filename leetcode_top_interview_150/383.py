# https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_letters_map = {}

        for char in magazine:
            if char in magazine_letters_map.keys():
                magazine_letters_map[char] = magazine_letters_map[char] + 1
            else:
                magazine_letters_map[char] = 1

        for char_rn in ransomNote:
            if not char_rn in magazine_letters_map.keys():
                return False

            magazine_letters_map[char_rn] = magazine_letters_map[char_rn] - 1
            
            if magazine_letters_map[char_rn] < 0:
                return False

        return True