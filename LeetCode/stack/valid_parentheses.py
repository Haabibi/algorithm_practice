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
        """
        pair = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for char in s:
            if char in pair.keys():
                stack.append(char)
            else:
                if len(stack) > 0 and char == pair[stack[-1]]:
                    # if there is a matching pair
                    stack.pop()
                else:
                    stack.append(char)
        if len(stack) == 0:
            return True
        else:
            return False
