#!/usr/bin/python3
"""Read and print a text file."""


def read_file(filename=""):
    """Read a text file and print its contents to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
