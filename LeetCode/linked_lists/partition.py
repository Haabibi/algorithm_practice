"""
86. Partition List
[Medium]
https://leetcode.com/problems/partition-list/

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        
        >>> s = Solution()
        >>> appendLL(s.partition(createLL([1,4,3,2,5,2]), 3))
        [1, 2, 2, 4, 3, 5]
        >>> appendLL(s.partition(createLL([]), 3))
        []
        >>> appendLL(s.partition(createLL([1]), 3))
        [1]
        >>> appendLL(s.partition(createLL([1,3]), 3))
        [1, 3]
        >>> appendLL(s.partition(createLL([1, 3, 2, 2, 2, 2, 2]), 3))
        [1, 2, 2, 2, 2, 2, 3]

        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        if head == None or head.next == None:
          return head
        
        smaller = ListNode(0)
        dummy1 = smaller 
        bigger = ListNode(0)
        dummy2 = bigger
        
        while head:
          if head.val < x:
            smaller.next = head
            smaller = smaller.next
            
          else: 
            # cur_head.val >= x
            bigger.next = head
            bigger = bigger.next
             
          head = head.next

        bigger.next = None
        smaller.next = dummy2.next
        
        
        return dummy1.next

if __name__=='__main__':
    import doctest
    from helper_functions import createLinkedList as createLL
    from helper_functions import appendLinkedList as appendLL

    doctest.testmod()
