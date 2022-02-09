"""
13. Roman to Integer
Difficulty: Easy

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together.
12 is written as XII, which is simply X + II. The number 27 is written as XXVII,
which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However
the numeral for four is not IIII. Instead, the number four is written as IV. Because the
one is before the five we subtract it making four. The same principle applies to the number
nine, which is written as IX. There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
"""


class Solution:
    def romanToInt(self, s):
        """
        Complexity Analysis.
        Time: O(n) where n is the length of the string.
        Space: O(1). Here we use only a constant length of hashmap irrespective
                     of the size of the input.
        """

        # create a mapping between Roman and Integer
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        # the first element of the roman string is stored directly
        number = roman[s[0]]

        # iterate through the string except the first character
        for i in range(1, len(s)):
            a, b = roman[s[i]], roman[s[i - 1]]

            # NOTE: Roman strings always go from largest to smallest
            # if the value of the current character is greater than the
            # value of the previous character, it is something like "IX" etc.
            if a > b:
                number = number - b + (a-b)
            # else simply add the integer mapped to the roman value.
            else:
                number += a

        return number
