"""
Given an image represented by an NxN matrix, 
where each pixel in the image is 4 bytes, 
write a method to rotate the image by 90 degrees. 
Can you do this in place?

1 2     -->    3 1  or  2 4
3 4            4 2      1 3  
Input1: 
[
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
]
"""

def clockwise_rotate(matrix):
    """
    Transpose the matrix first 

    """
    # transpose matrix
    transpose_matrix = [[matrix[row_idx][col_idx] for row_idx in range(len(matrix))] for col_idx in range(len(matrix[0]))]

    # flip cols
    #flip_matrix = [[matrix[i][len(matrix-j)] for i in range(len(matrix))] for j in range(len(matrix[0])) ]
    #print(flip_matrix) 
        
    
    return flip_matrix

def counter_clockwise_rotate(matrix):
    """
    Transpose the matrix first
    Flip items horizontally 

    1 2 3   M.T   1 4 7   Flip  3 6 9 
    4 5 6   --->  2 5 8  -----> 2 5 8
    7 8 9         3 6 9         1 4 7
    
    INPUT1 = [ 
                [1, 2, 3],
                [4, 0, 0],
                [7, 8, 9],
            ]
    >>> counter_clockwise_rotate(INPUT1)
    [[[3, 0, 9]], [[2, 0, 8]], [[1, 4, 7]]]

    """
    # transpose matrix
    transpose_matrix = [[matrix[row_idx][col_idx] for row_idx in range(len(matrix))] for col_idx in range(len(matrix[0]))]

    # flip rows
    flip_matrix = [[transpose_matrix[i]] for i in range(len(transpose_matrix)-1,-1,-1)]

    return flip_matrix


# counter-clockwise: [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0])-1, -1,-1)]   # j: row / i: col            
# matrix transpose -> flip the row: clockwise
# matrix transpose -> flip the col: counter-clockwise


if __name__=='__main__':
    INPUT1 = [ 
                [1, 2, 3],
                [4, 0, 0],
                [7, 8, 9],
            ]
    print(clockwise_rotate(INPUT1))

    import doctest
    doctest.testmod()
