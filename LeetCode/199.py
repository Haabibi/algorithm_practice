"""
199. Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

"""

class Solution(object):
    def rightSideView(self, root):
            """
            :type root: TreeNode
            :rtype: List[int]
            Time Complexity: O(N)
            - iterating all the nodes in the tree
            Space Complexity: O(N)
            - putting nodes from each layer into deque
            """
            from collections import deque 
            if root == None: 
              return []
            
            right_side = []
            prev_level  = deque([root])
            
            while len(prev_level) != 0:
              for _ in range(len(prev_level)):
                node = prev_level.popleft()
                if node.left:
                  prev_level.append(node.left)
                if node.right:
                  prev_level.append(node.right)
              
              # appending only the last added node value
              right_side.append(node.val)
            return right_side
