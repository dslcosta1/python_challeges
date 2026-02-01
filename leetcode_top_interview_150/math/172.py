class Solution:
    def trailingZeroes(self, n: int) -> int:
        count_fives = 0
        a = 1

        while 5**a <= n:
            five_exp = 5**a
            m = n//five_exp

            count_fives += m
            a += 1
        
        return count_fives

# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 -> 2
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 -> 4
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25 -> 6