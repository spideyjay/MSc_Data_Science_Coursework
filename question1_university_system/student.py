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

#The Student class needs to manage the courses a student is enrolled in and track their academic performance. 
#The calculate_gpa() method should be able to handle grades from multiple semesters.

#(inside the Student class)

    def enroll_course(self, course):
        """
        Enrolls the student in a course.
        """
        if course not in self._enrolled_courses:
            self._enrolled_courses.append(course)
            print(f"{self._name} has been enrolled in {course.name}.")
        else:
            print(f"{self._name} is already enrolled in {course.name}.")

    def drop_course(self, course):
        """
        Drops a course for the student.
        """
        if course in self._enrolled_courses:
            self._enrolled_courses.remove(course)
            print(f"{self._name} has dropped {course.name}.")
        else:
            print(f"{self._name} is not enrolled in {course.name}.")

    def calculate_gpa(self):
        """
        Calculates the student's GPA based on grades and course credits.
        This method can be enhanced to handle weighted grades and multiple semesters.
        """
        # assuming a simple grading system.
        grades = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
        total_points = 0
        total_credits = 0
        
        # Example of how to iterate through grades (assuming a grades list is added)
        # for grade, credits in self._grades:
        #     if grade in grades:
        #         total_points += grades[grade] * credits
        #         total_credits += credits

        # if total_credits > 0:
        #     self._gpa = total_points / total_credits
        # else:
        #     self._gpa = 0.0
        
        # For now, let's keep a placeholder
        pass

    # method to check the student's GPA and return their academic standing.
    
    @property
    def gpa(self):
        return self._gpa

    def get_academic_status(self):
        """
        Returns the student's academic status based on their GPA.
        """
        if self._gpa >= 3.5:
            return "Dean's List"
        elif 2.0 <= self._gpa < 3.5:
            return "Good Standing"
        else:
            return "Probation"