#!/usr/bin/python3
"""This module defines a Rectangle class that inherits from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class defines a rectangle."""

    def __init__(self, width, height):
        """Initialize a rectangle with validated width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
