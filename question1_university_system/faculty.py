# university_system/faculty.py

from .person import Person

class Faculty(Person):
    """
    A class to represent a faculty member in the university system.
    """
    def __init__(self, name, id_number, email):
        super().__init__(name, id_number, email)
        self._assigned_courses = []

    def get_responsibilities(self):
        """
        Overrides the base method to define faculty responsibilities.
        """
        return "Teaching classes, advising students, and participating in departmental meetings."

class Professor(Faculty):
    def __init__(self, name, id_number, email):
        super().__init__(name, id_number, email)

class Lecturer(Faculty):
    def __init__(self, name, id_number, email):
        super().__init__(name, id_number, email)

class TA(Faculty):
    def __init__(self, name, id_number, email):
        super().__init__(name, id_number, email)