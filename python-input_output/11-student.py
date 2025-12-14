#!/usr/bin/python3
"""Define a Student class with JSON serialization and deserialization."""


class Student:
    """Student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of the Student.

        If attrs is a list, only attributes in attrs are returned.
        """
        if isinstance(attrs, list):
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result
        return self.__dict__

    def reload_from_json(self, json):
        """Replace attributes of the Student instance from a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
