# rotate first ring of the matrix

from os import *
from sys import *
from collections import *
from math import *


def rotateMatrix(mat, n, m):
    row = 0
    col = 0
    while (row < n and col < m):

        # If we have rotated the whole matrix
        if (row == n - 1 or col == m - 1):
            break

        # Store the first element of next row as this element will replace first element of current row
        previous = mat[row + 1][col]

        # Move elements of first row from the remaining rows
        for i in range(col, m):
            current = mat[row][i]
            mat[row][i] = previous
            previous = current

        row += 1

        # Move elements of last column from the remaining columns
        for i in range(row, n):
            current = mat[i][m - 1]
            mat[i][m - 1] = previous
            previous = current

        m -= 1

        # Move elements of last row from the remaining rows
        if (row < n):
            for i in range(m - 1, col - 1, -1):
                current = mat[n - 1][i]
                mat[n - 1][i] = previous
                previous = current

        n -= 1

        # Move elements of first column from the remaining rows
        if (col < m):
            for i in range(n - 1, row - 1, -1):
                current = mat[i][col]
                mat[i][col] = previous
                previous = current

        col += 1
