"""
Given two strings, write a method to decide if one is a permutation of the other. 

Type: String1, String2 --> Boolean 

INPUT -> OUTPUT
'', '' -> True
'a', '' -> False
'a', 'a' -> True
'abc', 'cab' ->  True
'abcd', 'cab' -> False
'a', 'bc' -> False

Requirements of Permutation?
1. Two strings have same length
2. Same number of characters 

Questions?
1. Case sensitive?
2. Allow other data structures other than array & string?

"""

def check_permutation(str1, str2):
    """
    Implementation:
    - make each string into array
    - check the length of arrays & if they differ, return False
    - sort the arrays
    - if two arrays are same, return True
    
    >>> check_permutation('', '')
    True
    >>> check_permutation('a', '')
    False
    >>> check_permutation('a', 'a')
    True
    >>> check_permutation('abc', 'cab')
    True
    >>> check_permutation('abcd', 'cab')
    False
    >>> check_permutation('a', 'bc')
    False
    
    Time Complexity: O(N + N + 1) = O(N)
    Space Complexity: O(N + N) = O(N)
    """

    list1 = [x for x in str1]
    list2 = [x for x in str2]

    if sorted(list1) == sorted(list2):
        return True

    return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()
