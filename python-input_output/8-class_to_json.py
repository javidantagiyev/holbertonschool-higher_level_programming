#!/usr/bin/python3
"""Return the dictionary description of an object for JSON serialization."""


def class_to_json(obj):
    """Return the dictionary description of a simple data structure."""
    return obj.__dict__
