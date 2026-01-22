#!/usr/bin/python3
"""
This module provides a function that prints a square using the # character.

The size of the square must be a non-negative integer.
"""


def print_square(size):
    """
    Prints a square of size x size using the # character.

    Args:
        size (int): size of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)

