#!/usr/bin/python3
"""
This module provides a function to add two integers.

The function handles integers and floats, casting floats to integers
before performing the addition.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    a and b must be integers or floats. Floats are cast to integers
    before the addition. Otherwise, a TypeError is raised.

    Args:
        a (int or float): first number
        b (int or float): second number

    Returns:
        int: the addition of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

