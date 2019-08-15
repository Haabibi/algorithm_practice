"""
141. Linked List Cycle

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.


Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        
        # INPUT / OUTPUT
        
        # IMPLEMENTATION
         - need to return bool showing existence of cycle in the linked list
        3 -> 2 -> 0 -> -4 
             ^    ^
             ^     ^
                        ^^
        - if two pointers point to the same node at the same time
        -> return True 
        """
        # 1   2   3   4   5   6   None
        #         s               f
        slow_pointer = head 
        fast_pointer = head 
        if head == None:
          return False
        
        
        while fast_pointer and fast_pointer.next:
          slow_pointer = slow_pointer.next
          fast_pointer = fast_pointer.next.next
          if slow_pointer == fast_pointer:
            return True
          
        return False
