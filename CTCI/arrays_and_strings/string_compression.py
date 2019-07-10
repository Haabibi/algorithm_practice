"""
"""

def string_compression(string):
    output = ''
    new_char = string[0]
    cnt = 1

    for char in string[1:]:
        if new_char == char:
            cnt += 1
        #elif char == string[-1]:
        #    cnt += 1

        else:
            output += new_char + str(cnt)
            new_char = char
            cnt = 1
    return output


if __name__=='__main__':
    import doctest
    # doctest.testmod()
    print(string_compression('a'))
    #print(string_compression('aabcccaab'))
