#!/usr/bin/env python3
from typing import List

"""
A function that perform a list of slices from a list
"""


def slice_me_up_2(list_: list):
    """
    a list of slices from a list
    """
    arr_1 = list_[0:2]
    arr_2 = list_[-5:]
    arr_3 = list_[1:6]
    print(f"The first two numbers of the array are:{arr_1}")
    print(f"The last five numbers of the array are: {arr_2}")
    print(f"The 2nd through 6th numbers of the array are: {arr_3}")
    return


def main():
    """main function"""
    arr = [9, 8, 2, 3, 9, 4, 1, 0, 3]
    print(slice_me_up_2(arr))

main()
