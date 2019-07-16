"""
Assume you have a method isSubstring which checks 
if one word is asubstring of another. 
Given two strings, s1 and s2, write code to check 
if s2 is a rotation of s1 using only one call to isSubstring 
(e.g.,"waterbottle"is a rotation of "erbottlewat").

TODO: FIND DIFFERENCE BETWEEN FIND & IN 
string matching: find / in 

Visualizing substring matching algorithm:  Naïve    KMP    Boyer-Moore
http://whocouldthat.be/visualizing-string-matching/


"""


def is_substring(s1, s2):
    if s1 in s2:
        return True


def string_rotation(s1, s2):
    """
    Implementation
    Double the initial string(s1), 
    check if s2 is a substring of 2*s1

    """

    return is_substring(s1 + s1, s2)


if __name__ == "__main__":
    print(string_rotation("erbottlewat", "waterbottle"))
