"""
2. Add Two Numbers
Difficulty: medium

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list. You may assume the two
numbers do not contain any leading zero, except the number 0 itself.

NOTE: l1 and l2 are linked lists.
Input: l1 = 2 -> 4 -> 3], l2 = 5 -> 6 -> 4
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.


"""


from termios import NL1


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        Complexity Analysis:
        Time: O(max(n1, n2)) where n1 and n2 are length of the two lists respectively.
              We only travel through the longest list once.
        Space: Excluding our resultant list, O(1) space complexity, we didn't use any other
              variables that depend on the length of the list.
        """
        # create a dummy node whose next will point to our resultant linked list
        dummy = ListNode(0)
        # create an iterable pointer.
        current = dummy

        # to preserver the heads of the input lists, store them in temporary variables.
        n1, n2 = l1, l2

        # the integer to be forwaded over to the next summation.
        carry = 0
        # iterate through the array till both of them are None
        while n1 is not None or n2 is not None:

            # if the value of the current node is None, this means that
            # in summation, it will be 0 else as is.
            # For example,
            # 3 -> 2 -> 1
            # 4 -> 1   (0)
            x = 0 if n1 is None else n1.val
            y = 0 if n2 is None else n2.val

            # summation is defined as addition of two numbers and the carry forward
            ans = carry + x + y

            # if the summed answer is more than 10, it first digit needs to be
            # carried over in the next iteration.
            carry = int(ans / 10)

            # add only the unit digit from the summed output to the resultant linked list
            current.next = ListNode(ans % 10)
            current = current.next

            # Traverse through both the nodes simultaneously only they aren't null.
            if n1 is not None:
                n1 = n1.next
            if n2 is not None:
                n2 = n2.next

        # after the iteration and summation, if carry still exists for the highest face value
        # we add it to the output list.
        if carry > 0:
            current.next = ListNode(carry)

        # return the start of the resultant list.
        return dummy.next
