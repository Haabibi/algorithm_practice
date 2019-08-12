"""
234. Palindrome Linked List
[Easy]
https://leetcode.com/problems/palindrome-linked-list/

Given a singly linked list, determine if it is a palindrome.

Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?

"""


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        >>> s = Solution()
        >>> s.isPalindrome(create([1]))
        True
        >>> s.isPalindrome(create([1, 2]))
        False
        >>> s.isPalindrome(create([1, 3, 1]))
        True
        >>> s.isPalindrome(create([]))
        True
        >>> s.isPalindrome(create([1, 2, 3, 3, 2, 1]))
        True
        >>> s.isPalindrome(create([1, 1, 1, 1]))
        True
        >>> s.isPalindrome(create([1, 1, 1]))
        True
        
        Time Complexity: O(N + N/2) ~= O(N)
        Space Complexity: O(N) 
        - not inplace
        - create an extra list with all the values in linked list nodes
        """
        list_items = []
        cur_head = head
        while cur_head:
            list_items.append(cur_head.val)
            cur_head = cur_head.next

        if len(list_items) == 0 or len(list_items) == 1:
            return True
        for i in range(int(len(list_items) / 2)):

            if list_items[i] != list_items[len(list_items) - 1 - i]:
                return False

        return True


if __name__ == "__main__":
    import doctest
    from helper_functions import createLinkedList as create

    doctest.testmod()
