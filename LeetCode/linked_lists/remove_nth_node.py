"""
19. Remove Nth Node From End of List

https://leetcode.com/problems/remove-nth-node-from-end-of-list/<Paste>

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:
Could you do this in one pass?

"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        if n is bigger than the length of linked list, 
        remove the first item 

        >>> s = Solution()
        >>> appendLinkedList(s.removeNthFromEnd(createLinkedList([1]), 1))
        []
        >>> appendLinkedList(s.removeNthFromEnd(createLinkedList([1, 2, 3, 4, 5]), 2))
        [1, 2, 3, 5]
        >>> appendLinkedList(s.removeNthFromEnd(createLinkedList([1, 2, 3, 4]), 5))
        [2, 3, 4]
        
        Time Complexity: O(N1 + N2) 
        - N1: traversing linked list to get length 
        - N2: traversing again until len-nth item 
        Space Complexity: O(1)
        - inplace 
        """

        # find the length of a given linked list
        cur_head = head
        total_len = 0
        while cur_head:
            total_len += 1
            cur_head = cur_head.next

        # traverse from the beginning and find the nth elem from the end
        from_front_idx = total_len - n - 1

        cur_head = head
        while from_front_idx > 0 and cur_head:
            from_front_idx -= 1
            cur_head = cur_head.next

        if from_front_idx < 0:
            return cur_head.next
        else:
            cur_head.next = cur_head.next.next
            cur_head = cur_head.next

        return head


if __name__ == "__main__":
    import doctest
    from helper_functions import createLinkedList, appendLinkedList

    doctest.testmod()
