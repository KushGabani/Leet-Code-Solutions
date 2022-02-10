"""
19. Remove the nth node from the end of the list
Difficulty: Medium

Given the head of a linked list, remove the nth node from the end of the list
and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
"""


class ListNode:
    def __init__(self, val=0, link=None):
        self.val = val
        self.next = link


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        Complexity Analysis:
        Time: O(n), where n is the number of nodes in the linked list.
        Space: O(1)
        """
        # create a dummy node whose next will point to the head of the list
        dummy = ListNode()
        dummy.next = head

        # there will be two pointers, the current pointer will normally traverse
        # through the array till it reached null
        # the prev pointer will only move n nodes apart from the current pointer,
        # at the end of the loop, the previous will point to the previous of the node
        # to be deleted.
        prev = dummy
        curr = dummy.next

        i = 0
        while curr is not None:
            curr = curr.next
            i += 1
            if i > n:
                prev = prev.next

        # once we reach the previous node of the node to be deleted, we simply skip the nth node from the end
        prev.next = prev.next.next

        # return the head of the list.
        return dummy.next
