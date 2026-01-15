#!/usr/bin/python3
def fizzbuzz():
    """Print numbers from 1 to 100 with FizzBuzz rules.

    - Multiples of 3: print "Fizz"
    - Multiples of 5: print "Buzz"
    - Multiples of 3 and 5: print "FizzBuzz"
    Each element is separated by a space.
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
