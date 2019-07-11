"""
Write a method to replace all spaces in a string with '%20'. 
You may assume that the string has sufficient space at the end 
to hold the additional characters, and that you are given 
the 'true' length of the string. 

example input & output
Input: 'Mr John Smith    ', 13
Output: 'Mr%20John%20Smith'

Type: String, Int -> String 

* Assume there is no space at the front
* Assume there can only exist one space between words
* String with only space is not allowed 
  ex) '  ', 2 -X-> '%20%20'

Input -> Output
'a ', 1 -> 'a'
'a  ', 2 -> '%20a'
'a  ', 1 -> 'a'

"""

def urlify(url, length):
    """
    >>> urlify('Mr John Smith    ', 13)
    'Mr%20John%20Smith'
    >>> urlify('Mr John Smith    ', 14)
    'Mr%20John%20Smith%20'
    >>> urlify(' Mr John Smith    ', 14)
    'Mr%20John%20Smith%20'
    """
    
    trimmed_list = url.split(' ')
    new_list = []
    idx = 0
    while length >= 0:
        new_list.append(trimmed_list[idx])
        if trimmed_list[idx] == '':
            length -= 1
        else:
            length -= len(trimmed_list[idx])
            length -= 1 # space between words
        idx += 1
    
    
    output = reduce(lambda x, y: x +'%20'+ y, new_list)
    
    return output 

if __name__=='__main__':
    import doctest
    from functools import reduce
    doctest.testmod()
