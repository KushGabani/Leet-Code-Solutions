"""
15. 3 Sum
Difficulty: Medium

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""


class Solution:
    def threeSum(self, nums):
        """
        Complexity Analysis:
        Time: O(n^2) where n is the number of elements in nums.
        Space: Excluding the resultant array, it is O(1).
        """
        # sort the array in ascending order
        nums.sort()

        triplets = []

        i = 0
        # for each element in the array we find it's complementary pair
        # if it exists, we push all three in the output array.
        while i < len(nums):
            left = i + 1
            right = len(nums) - 1

            while(left < right):
                if nums[left] + nums[right] == -nums[i]:
                    triplets.append([nums[left], nums[right], nums[i]])

                    while left + 1 < right and nums[left + 1] == nums[left]:
                        left += 1

                    while right - 1 > left and nums[right - 1] == nums[right]:
                        right -= 1

                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < -nums[i]:
                    left += 1
                else:
                    right -= 1

            while i + 1 < len(nums) and nums[i+1] == nums[i]:
                i += 1

            i += 1
        return triplets


sol = Solution()
print(sol.threeSum([1, -1, -1, 0]))
