"""
98. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        
        Idea:
        left side always less than or equal to the parent node 
        right side always bigger than the parent node
        if it doesnt' pass return False
        return True when leaves reach to None 
        
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        if not root:
          return True 
        
        stack = []
        ma = float("inf")
        mi = float("-inf")
        stack.append((root, mi, ma))
        
        while stack:
            node, mi, ma = stack.pop()
            if node.val <= mi or node.val >= ma:
                return False
            if node.left:
                if node.left.val >= node.val:
                    return False
                else:
                    stack.append((node.left, mi, min(ma,node.val)))
            if node.right:       
                if node.right.val <= node.val:
                    return False
                else:
                    stack.append((node.right, max(mi,node.val), ma))
                    
        return True
       
