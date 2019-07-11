"""
Implement a method to perform basic string compression using the counts of repeated characters. 
For example, the string aabcccccaaa would become a2b1c5a3. 
If the "compressed" string would not become smaller 
than the original string, your method should return the original string. 
You can assume the string has only uppercase and lowercase letters (a - z).

INPUT -> OUTPUT
STRING -> STRING
'aabcccccaaa' -> 'a2b1c5a3'
'a' -> 'a1'
'ab' -> 'a1b1'
'aaa' -> 'a3' 
'' -> '' 

"""

def compress_string(string):
    """
    Implementation 
    - set the current_char 
    - iterate through string
    - if the iterated char equals to current_char
        - increase the counter
    - if not, 
        - append the current_car and the counter to the output string

    * dealing with edge cases
    - when there is only one char
        - return the char + cnt
    - when there is no character
        - return nothing 
    
    >>> compress_string('aabcccccaaa' )
    'a2b1c5a3'
    >>> compress_string('a')
    'a1'
    >>> compress_string('ab')
    'a1b1'
    >>> compress_string('aaa')
    'a3' 
    >>> compress_string('')
    '' 

    """
    # Type Checking
    if not isinstance(string, str):
        raise AssertionError("WRONG INPUT TYPE")

    if len(string) == 0:
        return ''
    
    new_char = string[0]
    output = new_char
    cnt = 1
    
    # iterate from the second char to the second to the last
    for char in string[1:]:
        if new_char == char:
            cnt += 1
        else:
            # new_char != char -> meaning, new char is observed
            # append the counter for the previous char
            output +=  str(cnt)
            # set the counter back to 1 and new_char to new encountered char
            cnt = 1
            new_char = char
            # append the newly encountered char
            output += new_char
            
    if cnt>0:
        output += str(cnt)

    return output

if __name__=='__main__':
    import doctest
    doctest.testmod()
