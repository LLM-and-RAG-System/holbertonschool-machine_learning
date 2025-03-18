#!/usr/bin/env python3
'''defines a function that adds two arrays element-wise'''
def add_arrays(arr1, arr2):
    '''add two arrays element-wise'''
    if len(arr1) != len(arr2):
        print('Array not the same size')
        return None
    return [arr1[i] + arr2[i] for i in range(len(arr1))]