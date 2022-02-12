"""
58. Length of the last word
Difficulty: Easy

Given a string s consisting of some words separated by some number of spaces,
return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
"""

class Solution:
    def lengthOfLastWord(self, s):
        """
        Complexity Analysis:
        Time: O(n), where n is the length of s. At the worst case, s is only a single word
             and we have to iterate through it, so time complexity is O(n).
        Space: O(1).
        """

        # a variable to maintain the length of the last word
        length = 0
        # to keep track if string s contains trailing spaces
        trailing_space = True

        # iterate through the string in reverse
        for i in range(len(s) - 1, -1, -1):

            # if the current character is a trailing space, skip it.
            if s[i] == " " and trailing_space:
                continue

            # if the current character is a char and trailing spaces have been skipped,
            # set trailing spaces to False
            elif s[i] != " " and trailing_space:
                trailing_space = False
            
            # if the current character is a char, increment the length of the last word
            if s[i] != " ":
                length += 1
            # if they encounter a space, return the length of the last word
            else:
                break
        
        return length
            