"""
There are three types of edits that can be performed on strings: 
insert a character, remove a character, or replace a character. 
Given two strings, write a function to check 
if they are one edit (or zero edits) away.

TYPE: STRING, STRING -> BOOL

(EX) INPUT -> OUTPUT
pale, ple -> True
pales, pale -> True
pale, bale -> True
pale, bake -> False

- shouldn't just get the intersection of two strings
- need to consider the order of the chars too

"""

def one_away(str1, str2):
    """
    Implementation
    - compare length of two strings
    - iterate through a string that is longer
    - have pointers on each string
    - increase the counter when difference is found 
    >>> one_away('pale', 'ple')
    True
    >>> one_away('pales', 'pale')
    True
    >>> one_away('pale', 'bale')
    True
    >>> one_away('pale', 'bake')
    False

    """


    # if two strings are exactly same -> return False
    if str1 == str2:
        return False

    # if two lengths differ 
    if len(str1) != len(str2):
        
        # if length of strings differ by more than one
        if abs(len(str1) - len(str2)) > 1:
            return False
        
        # compare length of two strings
        if len(str1) > len(str2):
            longer_str, shorter_str = str1, str2
        else:
            longer_str, shorter_str = str2, str1
        
        for i in range(len(longer_str)):
            if longer_str[:i] + longer_str[i+1:] == shorter_str:
                return True
        return False
    else:
        diff = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                diff += 1
        return False if diff >1 else True
if __name__=='__main__':
    import doctest
    doctest.testmod()
