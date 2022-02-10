"""
20. Valid Parenthesis
Difficulty: Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Input: s = "()[]{}"
Output: true


Input: s = "(]"
Output: false
"""


class Solution:
    def isValid(self, s):
        """
        Complexity Analysis:
        Time: O(n), where n is the length of the string.
        Space: O(1). 
        """

        # if the string is empty, then it is already a valid string
        if s == "":
            return True

        # create a mapping of opening and closing parens
        paren = {
            '(': ')',
            '{': '}',
            '[': ']',
        }

        # a stack to store the most recent opening paren
        stack = []

        # iterate through each bracket in the string
        for ch in s:
            # if the bracket is an opening bracket, simply add it to the stack
            if ch in ['(', '[', '{']:
                stack.append(ch)

            # if the bracket is a closing bracket,
            else:
                # if the stack isn't empty, perform a pop operation and compare it to its corresponding bracket.
                if len(stack) != 0:
                    element = stack.pop()
                    if paren[element] != ch:
                        return False
                else:
                    return False

        # if the stack is empty i.e. no parens pairs are left, the string is valid
        if len(stack) == 0:
            return True

        return False
