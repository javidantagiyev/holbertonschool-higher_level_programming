#!/usr/bin/python3
import pickle


class CustomObject:
    """Custom class for demonstrating pickling."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display object attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object and save it to a file."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (FileNotFoundError, pickle.PickleError, OSError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file and return it."""
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
        except (FileNotFoundError, pickle.PickleError, EOFError, OSError):
            return None

        return None
