#!/usr/bin/env python3
""" defines function that concatenates two 2D matrices along an axis """


def cat_matrices2D(mat1, mat2, axis=0):
    """Function that concatenates two 2D matrices along an axis"""
    if axis == 0 and len(mat1[0]) != len(mat2[0]):
        return None
    if axis == 1 and len(mat1) != len(mat2):
        return None
    if axis == 0:
        return [row.copy() for row in mat1] + [row.copy() for row in mat2]
    if axis == 1:
        return [mat1[i].copy() + mat2[i].copy() for i in range(len(mat1))]
    return None
