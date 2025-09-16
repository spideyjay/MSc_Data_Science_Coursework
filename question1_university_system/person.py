# university_system/person.py

class Person:
    """
    A base class to represent a person in the university system.
    """
    def __init__(self, name, id_number, email):
        self._name = name  # Private attribute for encapsulation
        self._id_number = id_number
        self._email = email

    def get_responsibilities(self):
        """
        Base method to be overridden by subclasses.
        """
        return "No specific responsibilities defined."