#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase followed by a new line.

    Args:
        str (str): string to convert and print
    """
    result = ""
    for c in str:
        # Si c est une lettre minuscule, convertir en majuscule
        if ord('a') <= ord(c) <= ord('z'):
            result += chr(ord(c) - 32)
        else:
            result += c
    print("{}".format(result))
