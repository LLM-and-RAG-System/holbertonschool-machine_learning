#!/usr/bin/env python3
""" defines function that performs matrix multiplication """
def mat_mul(mat1, mat2):
    """Function that performs matrix multiplication"""
    row = len(mat1)
    col = len(mat2[0])
    if row != col:
        return None
    return [
        [sum(a * b for a, b in zip(row, col)) for col in zip(*mat2)]
        for row in mat1
    ]