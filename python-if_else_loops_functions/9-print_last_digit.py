#!/usr/bin/python3
def print_last_digit(number):
    """Print the last digit of a number and return it.

    Args:
        number (int): the number to process

    Returns:
        int: last digit of number
    """
    last_digit = abs(number) % 10  # obtenir le dernier chiffre
    print("{}".format(last_digit), end="")  # affichage sans saut de ligne
    return last_digit
