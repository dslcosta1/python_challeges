# https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def reverseWords(self, s: str) -> str:
        

        word = ""
        words = ""

        for c in s:
            if c == ' ':
                if len(word) > 0: words = word + " " + words
                word = ""
            else:
                word += c
        
        if len(word) > 0: words = word + " " + words

        return words[:-1]