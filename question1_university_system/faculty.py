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


# override the subclasses to provide specific behaviors
def get_responsibilities(self):
    return "Teaching advanced courses, conducting research, and advising graduate students."

# Inside Lecturer class in faculty.py
def get_responsibilities(self):
    return "Teaching undergraduate courses and preparing lecture materials."

# Inside TA class in faculty.py
def get_responsibilities(self):
    return "Assisting with labs and tutorials, and grading assignments."

# Inside Faculty class in faculty.py
def calculate_workload(self):
    return "Workload calculation is not defined for this faculty type."

# Inside Professor class in faculty.py
def calculate_workload(self):
    # Example calculation: 3 courses * 10 hours/course + 20 hours for research
    return (len(self._assigned_courses) * 10) + 20

# Inside Lecturer class in faculty.py
def calculate_workload(self):
    # Example calculation: 4 courses * 15 hours/course
    return len(self._assigned_courses) * 15

# Inside TA class in faculty.py
def calculate_workload(self):
    # Example calculation: 2 labs * 5 hours/lab + 10 hours for grading
    return (len(self._assigned_courses) * 5) + 10