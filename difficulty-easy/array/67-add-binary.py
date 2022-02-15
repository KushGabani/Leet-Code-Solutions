"""
67. Add Binary
Difficulty: Easy

Given two binary strings a and b, return their sum as a binary string.

Input: a = "11", b = "1"
Output: "100"

Input: a = "1010", b = "1011"
Output: "10101"

Constraints:
    1 <= a.length, b.length <= 104
    a and b consist only of '0' or '1' characters.
    Each string does not contain leading zeros except for the zero itself.
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Complexity Analysis:
        Time: O(n), where n is the length of the longer string.
        Space: O(1) if we exclude the return string we build throughout the process.
        """
        # iterate through the strings from the end to the beggining.

        ia = len(a) - 1
        ib = len(b) - 1

        # initialize output to an empty string and carry to zero because at the beginning
        # there is no carry.
        carry = 0
        output = ""

        # while the pointer indices does not reach the beginning of the string.
        while ia != -1 or ib != -1:

            # in case either of the string has reached the end, we need to fill the addition with 0.
            x = a[ia] if ia >= 0 else '0'
            y = b[ib] if ib >= 0 else '0'

            # integer addition of the two numbers and the carry.
            ans = int(x) + int(y) + carry

            # if the answer is greater than equal to 2, we need to carry.
            if ans >= 2:
                carry = 1
                ans -= 2  # subtract 2 because we need to get the remainder.
            else:
                carry = 0

            # append the answer to the beginning of the output
            output = str(ans) + output

            # update ia, ib
            if ia >= 0:
                ia -= 1
            if ib >= 0:
                ib -= 1

        # at the end, if still a carry over needs to be made, we need to add 1 to the beginning of the output.
        if carry == 1:
            output = '1' + output

        return output
