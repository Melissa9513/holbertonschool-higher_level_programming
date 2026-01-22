#!/usr/bin/python3
"""
This module provides a function that prints a text with indentation.

Two new lines are printed after each '.', '?' and ':' character.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?' and ':'.

    Args:
        text (str): the text to print

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""
    for char in text:
        line += char
        if char in ".?:":
            print(line.strip())
            print()
            line = ""

    if line:
        print(line.strip(), end="")

