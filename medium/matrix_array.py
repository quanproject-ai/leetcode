# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]


def answer(n): ## matrix[x][y] where x is refering to rows and y is referring to column
    if n <= 0: 
        return []
    matrix = [[0] * n for _ in range(n)]
    top, left = 0, 0 #starting point: going from top left! top most row and left most column
    bottom, right = n-1 , n-1 #referring to the max index (i.e. 3x3 matrix has max indexes of either rows or cols are 2)
    num = 1 # starting at 1 because that's the requirement
    while top <= bottom and left <= right: #this is to prevent the loops going out of max indexes
        # Fill top boundary from left to right
        for i in range(left, right + 1): 
            matrix[top][i] = num # row is kept constant, changing column value
            num += 1
        top += 1 #After filling the top row, top is incremented to move down to the next row.

        # Fill right boundary from top to bottom
        for i in range(top, bottom + 1): 
            matrix[i][right] = num #columns are kept constant, changing row value
            num += 1 
        right -= 1 #After filling the right column, right is decremented to move left to the previous column.

        # Fill the bottom boundary from right to left
        for i in range(right, left - 1, -1): 
            matrix[bottom][i] = num #row are kept constant, chagning columns value
            num += 1
        bottom -= 1 #After filling the bottom row, bottom is decremented to move up to the previous row.

        # Fill the left boundary from bottom to top
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num #columns are constant
            num += 1
        left += 1 #	After filling the left column, left is incremented to move right to the next column.
    return matrix

# >> 
#//
#<<
#^^


print(answer(3))

# print([i for i in range(1,1,-1)])