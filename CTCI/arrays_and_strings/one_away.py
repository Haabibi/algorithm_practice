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


"""

def one_away(str1, str2):
    """
    Implementation
    - iterate through a string that is longer
    - have pointers on each string
    - increase the counter when difference is found 

    

    """
    
    cnt = 0
    
    if abs(len(str1) - len(str2)) == 1:
        cnt += 1 
        

if __name__=='__main__':
    import doctest
    doctest.testmod()
