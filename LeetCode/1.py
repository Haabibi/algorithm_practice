"""
1. Two Sum
Easy
https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        Implementation
        
        iterate through nums  and check whether the complement of the current item to the target exists in the dictionary
        if it is, return the current item index and the index of the complement in the dictionary

        : time complexity: O(N+1) - for iterating through nums, 1 for finding elements in dictionary
        : space complexity: O(N) - for making a dictionary
        """
        num_set =  {}
        return_output = []
        for i in range(len(nums)):
          complement = target - nums[i]
          if complement in num_set.keys():
            return sorted([i, num_set[complement]])
          else:
            num_set[nums[i]] = i
        
        
