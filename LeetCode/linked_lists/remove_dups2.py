"""
82. Remove Duplicates from Sorted List II
Leetcode: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/ 

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:
Input: 1->2->3->3->4->4->5
Output: 1->2->5


Example 2:
Input: 1->1->1->2->3
Output: 2->3

"""


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
        >>> appendLinkedList(s.deleteDuplicates(createLinkedList([1, 2, 3])))
        [1, 2, 3]
        >>> appendLinkedList(s.deleteDuplicates(createLinkedList([1, 2, 3, 3, 4, 4, 5])))
        [1, 2, 5]
        >>> appendLinkedList(s.deleteDuplicates(createLinkedList([])))
        []
        >>> appendLinkedList(s.deleteDuplicates(createLinkedList([1,1,1,1,1])))
        []
        >>> appendLinkedList(s.deleteDuplicates(createLinkedList([1, 2, 2, 5])))
        [1, 5]
        >>> appendLinkedList(s.deleteDuplicates(createLinkedList([1, 1])))
        []
        
        Time Complexity: O(N) 
        Space Complexity: O(1) - inplace algorithm
        """
        dummy = ListNode(-1)
        dummy.next = head

        cur_head = dummy

        while cur_head and cur_head.next and cur_head.next.next:
            if cur_head.next.val == cur_head.next.next.val:
                next_tmp = cur_head.next.next.next
                while next_tmp and next_tmp.val == cur_head.next.val:
                    next_tmp = next_tmp.next
                cur_head.next = next_tmp

            else:
                cur_head = cur_head.next

        return dummy.next


if __name__ == "__main__":
    import doctest
    from helper_functions import createLinkedList, printLinkedList, appendLinkedList

    doctest.testmod()
