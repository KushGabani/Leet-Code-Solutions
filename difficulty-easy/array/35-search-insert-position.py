"""
35. Search Insert Position
Difficulty: Easy

Given a sorted array of distinct integers and a target value,
return the index if the target is found. If not, return the index where
it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Input: nums = [1,3,5,6], target = 5
Output: 2

Input: nums = [1,3,5,6], target = 2
Output: 1

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""


class Solution:
    def searchInsert(self, nums, target):
        """
        Complexity Analysis:
        Time: O(log n), where n is the length of the array. This is because we apply binary search
        Space: O(1)
        """
        # perform binary search on the already sorted array and find the position to insert
        left = 0
        right = len(nums) - 1

        # if the target is smaller than the minimum number, return the first index
        if nums[left] > target:
            return 0
        # if the target is bigger than the maximum number, return the new last index
        if nums[right] < target:
            return right + 1

        # while two pointers, does not cross each other..
        while(left <= right):

            # compute the mid element
            mid = (left + right) // 2

            # if the middle element is the target, return the index.
            if nums[mid] == target:
                return mid
            # if the target resides in the right half, shorten the sub array.
            if target > nums[mid]:
                left = mid + 1
            # if the target resides in the left half, shorten the sub array.
            else:
                right = mid - 1

        return right + 1


sol = Solution()
print(sol.searchInsert([-1, 3, 5, 6, 8], 7))
