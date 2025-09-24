# university_system/faculty.py
from person import Person
from typing import List
from typing import Dict

class Faculty(Person):
    """
    A class to represent a faculty member in the university system.
    """
    
    def __init__(self, name: str, id_number: str, email: str, department: str):
        super().__init__(name, id_number, email)
        self.department = department
        self._assigned_courses = []  # List of Course objects

    def get_responsibilities(self) -> str:
        return "Teach courses, advise students, conduct research, serve on committees"

    def calculate_workload(self) -> Dict:
        """Calculate workload with detailed breakdown."""
        total_credits = sum(course.credits for course in self._assigned_courses)
        
        workload = {
            'total_courses': len(self._assigned_courses),
            'total_credits': total_credits,
            'courses': [str(course) for course in self._assigned_courses],
            'workload_status': 'Normal' if total_credits <= 12 else 'Overloaded'
        }
        return workload

    def assign_course(self, course) -> bool:
        """Assign a course to this faculty member."""
        if course not in self._assigned_courses:
            self._assigned_courses.append(course)
            course.assign_faculty(self)
            return True
        return False

    def get_assigned_courses(self) -> List:
        return self._assigned_courses.copy()

    def can_teach_more(self) -> bool:
        """Check if faculty can teach more courses (max 4 courses)."""
        return len(self._assigned_courses) < 4


class Professor(Faculty):
    def get_responsibilities(self) -> str:
        return "Professor: Teach advanced courses, research, supervise PhDs, secure grants, publish"

    def calculate_workload(self) -> Dict:
        base_workload = super().calculate_workload()
        base_workload['research_commitment'] = 'High'
        base_workload['phd_supervision'] = 'Expected'
        return base_workload


class Lecturer(Faculty):
    def get_responsibilities(self) -> str:
        return "Lecturer: Teach undergraduate courses, curriculum development, student advising"

    def calculate_workload(self) -> Dict:
        base_workload = super().calculate_workload()
        base_workload['teaching_focus'] = 'Undergraduate'
        base_workload['research_expectation'] = 'Moderate'
        return base_workload


class TA(Faculty):
    def __init__(self, name: str, id_number: str, email: str, department: str, supervisor=None):
        super().__init__(name, id_number, email, department)
        self.supervisor = supervisor  # Professor who supervises this TA

    def get_responsibilities(self) -> str:
        responsibilities = "TA: Assist in teaching, grade assignments, hold office hours"
        if self.supervisor:
            responsibilities += f", assist {self.supervisor.name}"
        return responsibilities

    def calculate_workload(self) -> Dict:
        base_workload = super().calculate_workload()
        base_workload['max_courses'] = 2  # TAs have lower teaching loads
        base_workload['role'] = 'Teaching Assistant'
        return base_workload