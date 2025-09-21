# university_system/department.py

from .faculty import Faculty
from .course import Course

class Department:
    def __init__(self, name):
        self.name = name
        self.faculty_list = []
        self.course_list = []
        self.student_list = []

    def add_faculty(self, faculty):
        if isinstance(faculty, Faculty):
            self.faculty_list.append(faculty)

    def add_course(self, course):
        if isinstance(course, Course):
            self.course_list.append(course)

    def add_student(self, student):
        self.student_list.append(student)

    def assign_faculty_to_course(self, faculty, course):
        if faculty in self.faculty_list and course in self.course_list:
            course.assign_faculty(faculty)

    def assign_student_to_department(self, student):
        self.add_student(student)
