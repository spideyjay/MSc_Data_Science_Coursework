# university_system/student.py

from .person import Person # The dot means 'from the current directory'

class Student(Person):
    """
    A class to represent a student in the university system.
    """
    def __init__(self, name, id_number, email):
        super().__init__(name, id_number, email)
        self._enrolled_courses = []
        self._grades = {}  # {course_code: [grade1, grade2, ...]}
        self._gpa = 0.0

    def enroll_course(self, course):
        if len(self._enrolled_courses) >= 6:
            print("Enrollment limit reached!")
            return
        if course.add_student(self):
            self._enrolled_courses.append(course)
        else:
            print("Could not enroll: course full or prerequisites not met.")

    def drop_course(self, course):
        if course in self._enrolled_courses:
            self._enrolled_courses.remove(course)
            course.remove_student(self)

    def add_grade(self, course_code, grade):
        if course_code not in self._grades:
            self._grades[course_code] = []
        self._grades[course_code].append(grade)

    def calculate_gpa(self):
        total_points = 0
        total_courses = 0
        for grades in self._grades.values():
            for grade in grades:
                total_points += grade
                total_courses += 1
        self._gpa = round(total_points / total_courses, 2) if total_courses > 0 else 0.0
        return self._gpa

    def get_gpa(self):
        return self._gpa

    def get_academic_status(self):
        gpa = self.calculate_gpa()
        if gpa >= 3.7:
            return "Dean's List"
        elif gpa >= 2.0:
            return "Good Standing"
        else:
            return "Probation"

    def get_responsibilities(self):
        return "Attend classes, complete assignments, take exams"

class UndergraduateStudent(Student):
    def get_responsibilities(self):
        return "Undergraduate: Attend lectures, complete assignments, participate in clubs"

class GraduateStudent(Student):
    def get_responsibilities(self):
        return "Graduate: Research, attend seminars, assist in teaching"

# Encapsulation with validation
class SecureStudentRecord(Student):
    def __init__(self, name, id_number):
        super().__init__(name, id_number)
        self.__ssn = None  # private attribute

    def set_ssn(self, ssn):
        if isinstance(ssn, str) and len(ssn) == 9 and ssn.isdigit():
            self.__ssn = ssn
        else:
            raise ValueError("Invalid SSN")

    def get_ssn(self):
        return self.__ssn

    def set_gpa(self, gpa):
        if 0.0 <= gpa <= 4.0:
            self._gpa = gpa
        else:
            raise ValueError("GPA must be between 0.0 and 4.0")

    def get_gpa(self):
        return self._gpa