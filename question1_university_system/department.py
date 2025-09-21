# university_system/department.py

class Department:
    """
    A class to represent a university department.
    """
    def __init__(self, name):
        self._name = name
        self._faculty = []
        self._courses = []

# methods for managing faculty and courses


class Department:
    """
    A class to represent a university department.
    """
    def __init__(self, name):
        self._name = name
        self._faculty = []
        self._courses = []

    def add_faculty(self, faculty):
        self._faculty.append(faculty)

    def add_course(self, course):
        self._courses.append(course)