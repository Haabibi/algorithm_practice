"""
61. Rotate List
Medium
https://leetcode.com/problems/rotate-list/

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL


Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        
        Input: 1->Null, k=1
        Output: 1->Null
        
        Input: 1->2->Null, k=1
        Output: 2->1->Null
        
        Input: 1->2->Null, k=2
        Output: 1->2->Null
        
        Implementation
        1. get the length of the whole linked list 
        2. if k > len(LL): k = k % len(LL)
        3. one pointer move len(LL) - k places
        Input: 1->2->3->4->5->NULL, k = 2
                     ^
                      3->None 
                         ^(new_head)
        len(LL) - k = 5 -2 = 3
        
        4. iterate through LL until it reaches none, 
          - set the pointer to the head 
        """
        if head == None:
          return None
        
        length_head = head
        length = 1
        
        while length_head.next:
          length += 1
          length_head = length_head.next 
          # length_head will be pointing to the end of the ll 

        if  k >= length:
          k = k % length
        
        # base cases where you can easily return
        if k == 0:
          return head 
        if length == 1 and k ==1:
          return head 
        
        cur_pointer = head 
        
        # move the cur_pointer 
        for _ in range(length-k-1):
          cur_pointer = cur_pointer.next
          
        new_head = cur_pointer.next 
        cur_pointer.next = None 
        length_head.next = head 
        # linking the last node of ll to the first node of ll 

        return new_head


