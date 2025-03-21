#!/usr/bin/env python3


def matrix_transpose(matrix):
    """
    A function that returns the transpose of a 2D matrix
    """
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]