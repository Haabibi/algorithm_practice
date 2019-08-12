"""
581. Shortest Unsorted Continuous Subarray
[EASY]
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.

"""


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        Implementation:
        1) scan from left to right and find the first element out of order
        2) scan from right to left and find the first elem out of order
        3) find local min/ local max in the subarray
        4) extend subarray on both ends to include any number bigger than min on the left / smaller than max on the right

        :type nums: List[int]
        :rtype: int

        Time Complexity: O(N1 + N2 + N3 + N4 + N5)
        - N1: traversing through left to right
        - N2: traversing through right to left 
        - N3: traversing subarray
        - N4: traversing from subarray to left to find nums bigger than min
        - N5: traversing from subarray to right to find nums less than max
        Space Complexity: O(N)
        - number of elements in new subarray 
        
        >>> s = Solution()
        >>> s.findUnsortedSubarray([1,2,3])
        0
        >>> s.findUnsortedSubarray([1, 3, 2, 3, 3])
        2
        >>> s.findUnsortedSubarray([1, 3, 2, 2, 2])
        4
        >>> s.findUnsortedSubarray([1, 2, 5, 3, 4])
        3
        >>> s.findUnsortedSubarray([1, 3, 2, 4, 5])
        2
        >>> s.findUnsortedSubarray([2, 1, 3])
        2
        >>> s.findUnsortedSubarray([2, 1])
        2
        >>> s.findUnsortedSubarray([1, 2])
        0
        """
        left_idx = 0
        right_idx = len(nums) - 1
        unsorted_flag = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                left_idx = i
                unsorted_flag = True
                break

        for j in range(len(nums) - 1, 0, -1):
            if nums[j] < nums[j - 1]:
                right_idx = j
                unsorted_flag = True
                break
        # print("Left_idx: {}, Right_idx: {}".format(left_idx, right_idx))

        if not unsorted_flag and left_idx == 0 and right_idx == len(nums) - 1:
            return 0

        # find local_min & local_max
        sub_array = nums[left_idx : right_idx + 1]
        local_min, local_max = sub_array[0], sub_array[0]
        for i in range(1, len(sub_array)):
            if local_min > sub_array[i]:
                local_min = sub_array[i]
            if local_max < sub_array[i]:
                local_max = sub_array[i]
        # print("Local Min, Local Max: ", local_min, local_max)

        for i in range(left_idx, -1, -1):
            if local_min < nums[i]:
                left_idx = i

        for j in range(right_idx + 1, len(nums)):
            if local_max > nums[j]:
                right_idx = j

        return len(nums[left_idx : right_idx + 1])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
