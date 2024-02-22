#!/usr/bin/python3
"""
    Implement 0x07 - Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """Rotates a 2d matrix"""

    for i in range(len(matrix)):
        for j in range(i, len(matrix[i])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(len(matrix)):
        matrix[i].reverse()
