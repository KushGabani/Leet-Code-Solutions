"""
1. Two Sum
Difficulty: Easy

Given an array of integers nums and an integer target, return indices of the two numbers
such that they add up to target. You may assume that each input would have exactly one
solution, and you may not use the same element twice. You can return the answer in any order.

https://leetcode.com/problems/two-sum/
"""


class Solution:
    def twoSum(self, nums, target):
        """
        Complexity Analysis:
        Time: O(n), where n is the length of the nums. We iterate through the array once
        Space: O(n), the space used by the hash table as the hashtable could possibly have to store
        all the variables in nums in the worst case.
        """

        # we create a hashtable/dictionary to keep track of whether we have seen its
        # complementary number before in the array.
        # for example, if the current element is 5 and target is 9. We will see if the key
        # 9 - 5 i.e. 4 exists in the hashtable. If it does, we have found the pair and we
        # will return its index.
        mem = {}

        # iterate through each values in the array
        for i in range(len(nums)):
            # find the complement that needs to be found in the array
            to_find = target - nums[i]

            # if the complement is found in the hashtable, we have found the pair.
            # Thus, we simply return a pair of the current index and the index of the
            if to_find in mem:
                return [mem[to_find], i]
            # If we don't, we will simply add the current index to the hashtable to keep history.
            mem[nums[i]] = i

        return []
