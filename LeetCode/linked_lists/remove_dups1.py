"""
83. Remove Duplicates from Sorted List
[EASY]
https://leetcode.com/problems/remove-duplicates-from-sorted-list/

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        >>> s = Solution()
        >>> printLinkedList(s.deleteDuplicates(createLinkedList([1, 2, 3, 3, 4, 5])))
        1->2->3->4->5
        >>> printLinkedList(s.deleteDuplicates(createLinkedList([])))
        
        >>> printLinkedList(s.deleteDuplicates(createLinkedList([1])))
        1
        """
        if head == None:
            return head

        cur_head = head
        next_head = head.next

        while next_head != None:
            if cur_head.val == next_head.val:
                cur_head.next = next_head.next
                next_head = next_head.next
            else:
                cur_head = cur_head.next
                next_head = next_head.next

        return head


if __name__ == "__main__":
    import doctest
    from helper_functions import createLinkedList, printLinkedList

    doctest.testmod()
