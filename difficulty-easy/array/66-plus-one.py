"""
66. Plus One
You are given a large integer represented as an integer array digits, where each digits[i]
is the ith digit of the integer. The digits are ordered from most significant to least
significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
"""

class Solution:
    def plusOne(self, digits):
        """
        Complexity Analysis:
        Time: O(n), where n is the length of the array.
        Space: O(1) because we are doing in-place operations.
        """

        # intialize the carry to one, as we want to add one number.
        carry = 1

        # we iterate the array from reverse i.e. from LSD to MSD
        # until carry is not zero.
        i = len(digits) - 1
        while i >= 0 and carry > 0:
            # store the summation in a temporary variable
            temp = digits[i] + carry

            # set the current digit to the LSD of the summation
            digits[i] = temp % 10

            # update the carry over if it exists
            carry = temp // 10
            i -= 1
        
        # if the iteration is completed and there is still a carry over,
        # insert the carry in the beginning of the array.
        if carry > 0:
            digits.insert(0, carry)

        return digits
