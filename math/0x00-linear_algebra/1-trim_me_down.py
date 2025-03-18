#!/usr/bin/env python3
from typing import List

"""
  A function that returns the middle column of a matrix
"""


def find_middle_column(list_: list) -> list:
    """
    A function that returns the middle column of a matrix
    """
    middel_column = len(list_[0]) // 2
    return [row[middel_column] for row in list_]


def main():
    """main function"""
    matrix = [[1, 3, 9, 4, 5, 8], [2, 4, 7, 3, 4, 0], [0, 3, 4, 6, 1, 5]]
    print(find_middle_column(matrix))


main()


"""
import numpy as np
def find_middle_column(matrix: List[List[int]]) -> List[int]:
    return np.array(matrix)[:, len(matrix) // 2].tolist()

"""
