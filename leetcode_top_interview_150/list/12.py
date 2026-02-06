class Solution:
    def intToRoman(self, num: int) -> str:

        divisors = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        
        roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        n = len(divisors)
        roman_number = []
        for i in range(n):
            while num >= divisors[i]:
                roman_number.append(roman[i])
                num -= divisors[i]

        return ''.join(roman_number)