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
* Assume there is only one space between words

Input -> Output
' ', 1 -> '%20' 
'  ', 2 -> '%20%20' 
'a ', 1 -> 'a'
'a  ', 2 -> '%20a'
'a  ', 1 -> 'a'

"""

def urlify(url, length):
    """
    Implementation:
    - Trim the end of the string 
    - 

    """
    trimmed_url = url.strip()
    trimmed_list = trimmed_url.split()
    final_str = ''
    for word in trimmed_list:
        final_str += word
        length -= len(word)

    return 

if __name__=='__main__':
    import doctest
    doctest.testmod()
