"""
69. Square Root of a Number
Difficulty: Easy

Find the square root of the integer without using built-in functions.
Return the truncated value of the integer if the square root is a decimal.

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated,
2 is returned.
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Complexity Analysis:
        Time: O(root(x)), where x is the input number.
        Space: O(1).
        """
        # a square root would only exist within the range of 0 to x / 2.
        # for edge cases like x = 1, we increment to 2 to x / 2
        for i in range(int(x / 2) + 2):
            # if the square of the number i is equal to the number x, and
            # the square of the number i + 1 is greater than x, we return i.
            if i * i <= x < (i + 1) * (i + 1):
                return i
