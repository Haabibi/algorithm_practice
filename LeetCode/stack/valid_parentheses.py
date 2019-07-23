"""
20. Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true

Example 2:

Input: "()[]{}"
Output: true

Example 3:

Input: "(]"
Output: false

Example 4:

Input: "([)]"
Output: false

Example 5:

Input: "{[]}"
Output: true
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        >>> s = Solution()
        >>> s.isValid('()')
        True
        >>> s.isValid('()[]{}')
        True
        >>> s.isValid(')}{({))[{{[}')
        False
        >>> s.isValid('){')
        False
        >>> s.isValid(')')
        False
        >>> s.isValid('){}')
        False

        Time Complexity: O(N)
        - traversing string 
        Space Complexity: O(N)
        - extra space for mapping parentheses pairs
        """
        stack = []
        pair_mapping = {")": "(", "}": "{", "]": "["}
          
        for char in s:
            if char in pair_mapping:
                if len(stack) == 0:
                    return False
                elif stack[-1] == pair_mapping[char]:
                    stack.pop()
                else:
                    stack.append(char)
            else:
              stack.append(char)
          
        if len(stack) == 0:
            return True
        else:
            return False

if __name__=='__main__':
    import doctest
    doctest.testmod()
