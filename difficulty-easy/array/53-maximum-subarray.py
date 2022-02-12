"""
53. Maximum Subarray
Difficulty: Easy

Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum. A subarray is a contiguous part of an array.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Input: nums = [1]
Output: 1

Constraints:
    1 <= nums.length <= 105
    -104 <= nums[i] <= 104

Follow up: If you have figured out the O(n) solution, try coding another solution using
the divide and conquer approach, which is more subtle.
"""

class Solution:
    def maxSubArray(self, nums):
        """
        Complexity Analysis:
        Time: O(n), where n is the length of the array
        Space: O(1)
        """
        max_so_far = nums[0]
        curr_max = nums[0]

        for i in range(1, len(nums)):
            curr_max = max(nums[i], nums[i] + curr_max)
            max_so_far = max(max_so_far, curr_max)
        
        return max_so_far
        