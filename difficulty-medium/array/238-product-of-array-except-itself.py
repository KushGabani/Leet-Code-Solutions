"""
238. Product of Array Except Self
Difficulty: medium

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements
of nums except nums[i]. The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

https://leetcode.com/problems/product-of-array-except-self
"""


class Solution:
    def productExceptSelf(self, nums):
        """
        Complexity Analysis:
        Time: O(n), where n is the length of nums. Here we iterate through the original array
              twice separately. Thus the complexity is O(n) + O(n) = O(n) time complexity.

        Space: Excluding the resultant array, there are no other variables used that depend
               on the size of nums. Thus the space complexity is O(1).
        """
        output = []

        # we will do two passes through the arrays separately.
        # the first pass will build an array of products of all
        # the elements before it.
        # in the next pass, we will start backwards and build an
        # array of products of all the elements before it from behind. This pass
        # will cover the products of all the elements after the current element.

        # the first pass
        curr_prod = 1
        # iterate through each element
        for num in nums:
            # we first append the current product to the output array and then
            # update the curr_prod so that the current element isn't included in
            # the product operation.
            output.append(curr_prod)

            # update the current product
            curr_prod *= num

        # second pass (reverse)
        # as mentioned, this will include all the items after the current element
        # in the product

        curr_prod = 1
        # iterate through the list backwards
        for i in range(len(nums) - 1, -1, -1):
            # update the product with the current product by multiplying it
            output[i] *= curr_prod

            # update the current product by multiplying it by the number.
            curr_prod *= nums[i]

        return output


sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))
