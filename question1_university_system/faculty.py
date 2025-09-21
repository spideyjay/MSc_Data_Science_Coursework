# university_system/faculty.py

from .person import Person

class Faculty(Person):
    """
    A class to represent a faculty member in the university system.
    """
    def __init__(self, name, id_number, email, department):
        super().__init__(name, id_number, email)
        self.department = department

    def get_responsibilities(self):
        return "Teach courses, advise students, conduct research"

    def calculate_workload(self):
        return "Standard faculty workload"

class Professor(Faculty):
    def get_responsibilities(self):
        return "Professor: Teach, research, supervise PhDs"

    def calculate_workload(self):
        return "Professor workload: 3 courses, research, supervision"

class Lecturer(Faculty):
    def get_responsibilities(self):
        return "Lecturer: Teach undergraduate courses"

    def calculate_workload(self):
        return "Lecturer workload: 4 courses"

class TA(Faculty):
    def get_responsibilities(self):
        return "TA: Assist in teaching, grade assignments"

    def calculate_workload(self):
        return "TA workload: Assist in 2 courses"
