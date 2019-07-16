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
    * Question: 
    matrix[row] = list(map(lambda x: x*0, matrix[row])) 
    this line seems to consume additional space 
    makes list first and replaces original nums to zero 
    Thus Space Complexity >> O(N + N*M), N: number of zero row / M: number of items inthe row  
    """

    zero_list = []
    for i in range(len(matrix)):  # row
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                zero_list.append((i, j))

    for index in zero_list:
        row, column = index
        # changing row to zero
        matrix[row] = list(map(lambda x: x * 0, matrix[row]))
        # changing col to zero
        for i in range(len(matrix)):
            matrix[i][column] = 0

    return matrix


# Improvement -
# the current implementation might change a row/column to already-zero-changed row/col
# which causes redundant computation
# try pruning zero_list!


def better_zero_matrix(better):
    """
    Implementation: Make a flag 
    - iterate through the matrix 
    - if zero is found, 
        - change the number in the first col/ row num to zero 
        ( X dynamically change? ) 
    - iterate through the first column / row 
        - if zero found in the first row,
            - change all the numbers in that column to zero
        - if zero found in the first col,
            - change all the numbers in that row to zero 
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
