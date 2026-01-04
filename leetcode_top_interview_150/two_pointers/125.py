# https://leetcode.com/problems/valid-palindrome/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for c in s:
            if c.isalnum():
                result += c.lower()

        result_reverse = result[::-1]
        return result == result_reverse