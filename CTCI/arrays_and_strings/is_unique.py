"""
Implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures?

Type: String --> Boolean 

Input --> Output
'' -> True
'a' -> True
'aa' -> False
'1%a' -> True
'aba' -> False
"""

def is_unique(test_str):
    """
    Brute Force Algorithm
    - Iterate through the string, and check whether a specific charcacter is in the rest of the string.
        - If there is, return False. 
        - If there isn't until the end of the test_str, return True. 

    Time Complexity: O(N^2)

    >>> is_unique('')
    True
    >>> is_unique('a') 
    True
    >>> is_unique('aa')
    False
    >>> is_unique('1%a') 
    True
    >>> is_unique('aba') 
    False
    >>> is_unique('hello') 
    False
    >>> is_unique('abcdefg') 
    True
    """
    
    for i in range(len(test_str)):
        for j in range(i+1, len(test_str)):
            if test_str[i] == test_str[j]:
                return False

    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
