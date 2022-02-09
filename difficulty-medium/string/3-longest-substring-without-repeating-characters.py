"""
3. Longest Substring Without Repeating Characters
Difficulty: Medium

Given a string s, find the length of the longest substring without repeating characters.
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Constraints
    0 <= s.length <= 5 * 10^4
    s consists of English letters, digits, symbols and spaces.

https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        Complexity Analysis:
        Time: O(n) where n is the length of the string. The entire string of length n is
              iterated only once.

        Space: O(n). We maisntain an additional variable which at the worst case will store the
               entire n-length input if it is distinct.
        """
        # we will keep building the non-repeating string
        mem = ""
        # a variable to store the maximum length of the non-repeating string
        max_len = 0

        # iterate through the string
        for i, ch in enumerate(s):

            # if the current character is already present in mem,
            # then its a repeating character and we need to remove the mem upto that point and
            # add the current character
            if ch in mem:
                mem = mem[mem.index(ch) + 1:] + ch

            # else simply build the non-repeating string
            else:
                mem += s[i]

            # after each iteration we see which one is longer, the current
            # non-repeating string or the biggest non-repeating string up until that point.
            # and store the biggest of the two as our new maximum length.
            max_len = max(max_len, len(mem))

        return max_len
