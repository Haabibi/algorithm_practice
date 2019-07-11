"""
Write an algorithm such that if an element in an MxN matrix is 0, 
its entire row and column are set to O.

TYPE: matrix -> matrix

1 2 3 4          1 0 3 4        
5 0 7 8     ->   0 0 0 0
9 10 11 12       9 0 11 12

"""

def zero_matrix(matrix):
    """
    Implementation
    - find where zeros are 
    - switch all numbers on the same row/column to 0 

    >>> zero_matrix([[1, 0, 3], [0, 5, 6], [7, 8 ,9]])
    [[0, 0, 0], [0, 0, 0], [0, 0, 9]]
    >>> zero_matrix([[1]])
    [[1]]
    >>> zero_matrix([])
    []
    >>> zero_matrix([[1, 2], [3, 4], [0, 5], [6, 7], [8,0]])
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    >>> zero_matrix([[1], [2], [3]])
    [[1], [2], [3]]

    Time Complexity: O(N1 + N2) - N1 for going through matrix to find indices of zeros
                                - N2 for going through zero_list to change into zeros
    Space Complexity: O(N) - N depending on the number of zeros /for making zero list/                           - X require additional space for matrix
    """

    zero_list = []
    for i in range(len(matrix)): # row
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                zero_list.append((i, j))
    
    for index in zero_list:
        row, column = index
        matrix[row] = list(map(lambda x: x*0, matrix[row]))
        for i in range(len(matrix)):
            matrix[i][column] = 0

    return matrix
if __name__=='__main__':
   import doctest
   doctest.testmod()

