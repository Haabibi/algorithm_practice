"""
2. Add Two Numbers
[MEDIUM]
https://leetcode.com/problems/add-two-numbers/description/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.


"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """	
        :type 
        - l1: ListNode
        - l2: ListNode
        :rtype ListNode 

	>>> s = Solution()
	>>> appendLinkedList(s.addTwoNumbers(createLinkedList([2, 4, 3]), createLinkedList([5, 6, 4])))
	[7, 0, 8]
	>>> appendLinkedList(s.addTwoNumbers(createLinkedList([1, 7]), createLinkedList([0])))
	[1, 7]
	>>> appendLinkedList(s.addTwoNumbers(createLinkedList([0, 1]), createLinkedList([5])))
	[5, 1]
	>>> appendLinkedList(s.addTwoNumbers(createLinkedList([4]), createLinkedList([6])))
	[0, 1]
	>>> appendLinkedList(s.addTwoNumbers(createLinkedList([9, 9]), createLinkedList([1])))
	[0, 0, 1]
	>>> appendLinkedList(s.addTwoNumbers(createLinkedList([5, 5, 2]), createLinkedList([5, 4, 1])))
	[0, 0, 4]
	
        Time Complexity: O(N1 + N2) 
        - N1: length of l1 
        - N2: length of l2
        Space Complexity: O(N) - creating new linked list where all nodes are added up
        """
        new_head = ListNode(-1)
        output = new_head
        carry = 0
        while True:
            tmp_val = l1.val + l2.val + carry
            if tmp_val > 9:
                carry = 1
            else:
                carry = 0

            new_head.val = tmp_val % 10

            if l1.next == None and l2.next == None:
                if carry == 1:
                    new_head.next = ListNode(1)
                    new_head = new_head.next
                break
            elif l1.next == None:
                l1.next = ListNode(0)
            elif l2.next == None:
                l2.next = ListNode(0)

            if l1.next and l2.next:
                l1 = l1.next
                l2 = l2.next
                new_head.next = ListNode(-1)
                new_head = new_head.next

        return output


if __name__ == "__main__":
    import doctest
    from helper_functions import createLinkedList, appendLinkedList

    doctest.testmod()
