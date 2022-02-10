"""
8. String to Integer (atoi)
Difficulty: Medium

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer
(similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

1. Read in and ignore any leading whitespace.
2. Check if the next character (if not already at the end of the string) is '-' or '+'.
   Read this character in if it is either. This determines if the final result is negative
   or positive respectively. Assume the result is positive if neither is present.
3. Read in next the characters until the next non-digit character or the end of the input
   is reached. The rest of the string is ignored.
4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits
   were read, then the integer is 0. Change the sign as necessary (from step 2).
5. If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the
   integer so that it remains in the range. Specifically, integers less than -231 should be
   clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
6. Return the integer as the final result.

NOTE:
Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string
after the digits.
"""


class Solution:
    def myAtoi(self, s):
        """
        Complexity Analysis:
        Time: O(n), where n is the length of the string.
        Space: O(1)
        """

        # check if the string is null or empty
        if s is None or s == "":
            return 0

        # initialize the result to 0
        result = 0
        # by default we assume the input string to be a positive integer.
        sign = 1

        # iterate through the string to skip the leading spaces until a character is hit.
        i = 0
        while(i < len(s) and s[i] == " "):
            i += 1

        if (i < len(s)):
            # check if the character is negative or positive after the leading spaces.
            if s[i] in ["-", "+"]:
                # if so we will turn the sign to -1 to represent negative
                sign = -1 if s[i] == "-" else 1
                i += 1

            # iterate through the rest of the s
            while(i < len(s) and s[i].isdigit()):
                result = result * 10 + int(s[i])

                # if at any point of time, the result is not in the range of an integer,
                # we clamp the result and return it.
                if result * sign < -2 ** 31:
                    return -2 ** 31
                if result * sign > 2 ** 31 - 1:
                    return 2 ** 31 - 1
                i += 1

        return result * sign
