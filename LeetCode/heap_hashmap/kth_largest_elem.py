"""
215. Kth Largest Element in an Array
Medium
https://leetcode.com/problems/kth-largest-element-in-an-array/

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    
    :time complexity: O(NlogN) - using python built-in sort function (Timsort)
    :space complexity: O(N) - Timsort requires a temp array containing as many as N//2 pointers
    -> worst case O(N), best case O(1)

    >>> findKthLargest(nums=[3,2,1,5,6,4], k = 2)
    5
    >>> findKthLargest(nums=[3,2,3,1,2,4,5,5,6], k = 4)
    4
    """
    nums = sorted(nums)
    return nums[len(nums)-k]

if __name__=='__main__':
    import doctest
    doctest.testmod()
