# university_system/student.py

from .person import Person # The dot means 'from the current directory'

class Student(Person):
    """
    A class to represent a student in the university system.
    """
    def __init__(self, name, id_number, email):
        super().__init__(name, id_number, email)
        self._enrolled_courses = []
        self._gpa = 0.0

    def get_responsibilities(self):
        """
        Overrides the base method to define student responsibilities.
        """
        return "Attending lectures, completing assignments, and preparing for exams."

class UndergraduateStudent(Student):
    def __init__(self, name, id_number, email):
        super().__init__(name, id_number, email)

class GraduateStudent(Student):
    def __init__(self, name, id_number, email):
        super().__init__(name, id_number, email)