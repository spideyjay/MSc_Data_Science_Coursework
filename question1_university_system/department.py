# university_system/department.py
from faculty import Faculty
from course import Course
from student import Student
from typing import List, Dict

class Department:
    """
    A class to represent a university department with enhanced management capabilities.
    """
    
    def __init__(self, name: str):
        self.name = name
        self.faculty_list = []
        self.course_list = []
        self.student_list = []

    def add_faculty(self, faculty: Faculty) -> bool:
        """Add faculty to department with validation."""
        if isinstance(faculty, Faculty):
            if faculty not in self.faculty_list:
                self.faculty_list.append(faculty)
                return True
        return False

    def add_course(self, course: Course) -> bool:
        """Add course to department offerings."""
        if isinstance(course, Course):
            if course not in self.course_list:
                self.course_list.append(course)
                return True
        return False

    def add_student(self, student: Student) -> bool:
        """Add student to department roster."""
        if student not in self.student_list:
            self.student_list.append(student)
            return True
        return False

    def assign_faculty_to_course(self, faculty: Faculty, course: Course) -> bool:
        """Assign faculty to teach a course with validation."""
        if (faculty in self.faculty_list and 
            course in self.course_list and 
            faculty.can_teach_more()):
            return faculty.assign_course(course)
        return False

    def assign_student_to_department(self, student: Student) -> bool:
        """Assign student to this department."""
        return self.add_student(student)

    def get_department_stats(self) -> Dict:
        """Get comprehensive department statistics."""
        return {
            'department': self.name,
            'faculty_count': len(self.faculty_list),
            'course_count': len(self.course_list),
            'student_count': len(self.student_list),
            'courses': [course.get_enrollment_info() for course in self.course_list],
            'faculty_workloads': [faculty.calculate_workload() for faculty in self.faculty_list]
        }

    def find_course(self, course_code: str) -> Course:
        """Find course by code."""
        for course in self.course_list:
            if course.code == course_code:
                return course
        raise ValueError(f"Course {course_code} not found in department")

    def get_overenrolled_courses(self) -> List[Course]:
        """Get courses that have students on waitlist."""
        return [course for course in self.course_list if course.waitlist]

    def __str__(self) -> str:
        return f"Department: {self.name} ({len(self.faculty_list)} faculty, {len(self.course_list)} courses, {len(self.student_list)} students)"

    def __repr__(self) -> str:
        return f"Department('{self.name}')"