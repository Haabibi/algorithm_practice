"""
Given a string, write a function to check 
if it is a permutation of a palindrome. 
A palindrome is a word or phrase that is the same forwards and backwards. 
A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.

TYPE: STRING -> BOOL 

(EX) Input - OUPUT:
Tact Coa -> True

Input -> Output
' ' -> True 
'a' -> True 
'ab' -> False
'aab' -> True ('aba')


Questions:
    1. No special characters?

"""

def is_permuted_palindrome(string):
    """
    Implementation
    whatver the word might be, as long as there are pairs of characters with one char,
    it would be regarded as permutation of a palindrome
    - receive an input
    - remove spaces and make all the chars into lowercase when changing the string > list (array of chars)
    - iterate through the list, delete the current char and the same char when found, 
    - if not found, move onto the next char
    - the total length of the list (array of chars) should be one or none to return True 

    >>> is_permuted_palindrome('Tact Coa')
    True
    >>> is_permuted_palindrome('taco cat')
    True
    >>> is_permuted_palindrome(' ')
    True
    >>> is_permuted_palindrome('a')
    True 
    >>> is_permuted_palindrome('ab')
    False
    >>> is_permuted_palindrome('aab')
    True 
    """
    
    test_str = [x.lower() for x in string if x!= ' ']
    pop_list = test_str

    for i in range(len(test_str)):
    #    print(i, len(test_str))
        for j in range(i+1, len(test_str)):
            print(i, j, test_str, len(test_str))
            if test_str[i] == test_str[j]:
                print("GOT HERE!", test_str[i], test_str[j])
                print("POP LIST1: ", pop_list)
                #pop_list.remove(test_str[j])
                del pop_list[j]
                print("POP LIST2: ", pop_list)
                #pop_list.remove(test_str[i])
                del pop_list[i]
                print("POP LIST3: ", pop_list)
                break
    if len(pop_list) <= 1:
        return True
    else:
        return False

if __name__=='__main__':
    import doctest
    # doctest.testmod()
    is_permuted_palindrome('Tact Coa')
