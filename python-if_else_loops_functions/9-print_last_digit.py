#!/usr/bin/python3
def print_last_digit(number):
    """Print and return the last digit of a number"""
    last = number % 10 if number >= 0 else -(-number % 10)
    print(last, end="")
    return last
