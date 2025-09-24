# university_system/student.py
import re
from person import Person
from typing import Dict, List, Optional

class Student(Person):
    """
    A class to represent a student in the university system with enhanced features.
    """
    
    MAX_COURSES = 6
    CREDITS_PER_COURSE = 3  # Default credits per course

    def __init__(self, name: str, id_number: str, email: str):
        super().__init__(name, id_number, email)
        self._enrolled_courses = []  # List of Course objects
        self._grades = {}  # {course_code: {'grades': [list], 'credits': int}}
        self._gpa = 0.0
        self._academic_status = "Good Standing"
        self._completed_credits = 0

    def enroll_course(self, course) -> bool:
        """Enroll student in a course with prerequisite checking and waitlist support."""
        if len(self._enrolled_courses) >= self.MAX_COURSES:
            raise ValueError(f"Enrollment limit reached! Maximum {self.MAX_COURSES} courses allowed.")
        
        # Check prerequisites
        missing_prereqs = self._check_prerequisites(course)
        if missing_prereqs:
            raise ValueError(f"Cannot enroll in {course.code}. Missing prerequisites: {missing_prereqs}")
        
        # Try to enroll (course handles capacity and waitlist)
        success = course.add_student(self)
        if success:
            self._enrolled_courses.append(course)
            print(f"Successfully enrolled in {course.code}")
            return True
        else:
            # Student added to waitlist by course
            print(f"Course {course.code} is full. Added to waitlist.")
            return False

    def _check_prerequisites(self, course) -> List[str]:
        """Check if student meets all prerequisites for a course."""
        missing = []
        for prereq in course.prerequisites:
            # Check if student has completed the prerequisite course
            if prereq not in self._grades or not self._is_course_passed(prereq):
                missing.append(prereq)
        return missing

    def _is_course_passed(self, course_code: str) -> bool:
        """Check if a course was passed (grade >= 2.0)."""
        if course_code in self._grades:
            grades = self._grades[course_code]['grades']
            avg_grade = sum(grades) / len(grades)
            return avg_grade >= 2.0
        return False

    def drop_course(self, course) -> bool:
        """Drop a course and notify waitlisted students."""
        if course in self._enrolled_courses:
            self._enrolled_courses.remove(course)
            course.remove_student(self)
            print(f"Dropped {course.code}")
            return True
        return False

    def add_grade(self, course_code: str, grade: float, credits: int = None) -> None:
        """Add grade for a course with credit-based calculation."""
        if not 0.0 <= grade <= 4.0:
            raise ValueError("Grade must be between 0.0 and 4.0")
        
        if credits is None:
            credits = self.CREDITS_PER_COURSE
        
        if course_code not in self._grades:
            self._grades[course_code] = {'grades': [], 'credits': credits}
        
        self._grades[course_code]['grades'].append(grade)
        self._update_academic_record()

    def _update_academic_record(self) -> None:
        """Update GPA and academic status after grade changes."""
        self._gpa = self.calculate_gpa()
        self._completed_credits = self._calculate_completed_credits()
        self._academic_status = self.get_academic_status()

    def calculate_gpa(self) -> float:
        """Calculate GPA using credit-weighted average."""
        total_quality_points = 0.0
        total_credits = 0
        
        for course_data in self._grades.values():
            grades = course_data['grades']
            credits = course_data['credits']
            
            if grades:  # Only include courses with grades
                course_avg = sum(grades) / len(grades)
                total_quality_points += course_avg * credits
                total_credits += credits
        
        return round(total_quality_points / total_credits, 2) if total_credits > 0 else 0.0

    def _calculate_completed_credits(self) -> int:
        """Calculate total completed credits."""
        return sum(data['credits'] for data in self._grades.values() if data['grades'])

    def get_academic_status(self) -> str:
        """Determine academic status based on GPA and credits."""
        gpa = self.calculate_gpa()
        
        if self._completed_credits >= 12 and gpa >= 3.7:
            return "Dean's List"
        elif gpa >= 2.0:
            return "Good Standing"
        elif gpa >= 1.5:
            return "Academic Probation"
        else:
            return "Academic Dismissal"

    def get_responsibilities(self) -> str:
        return "Attend classes, complete assignments, take exams"

    def get_transcript(self) -> Dict:
        """Generate a transcript with course details."""
        transcript = {
            'student': str(self),
            'gpa': self._gpa,
            'status': self._academic_status,
            'completed_credits': self._completed_credits,
            'courses': {}
        }
        
        for course_code, data in self._grades.items():
            if data['grades']:
                avg_grade = sum(data['grades']) / len(data['grades'])
                transcript['courses'][course_code] = {
                    'credits': data['credits'],
                    'average_grade': round(avg_grade, 2),
                    'grades': data['grades']
                }
        
        return transcript

    @property
    def gpa(self) -> float:
        return self._gpa

    @property
    def academic_status(self) -> str:
        return self._academic_status

    @property
    def completed_credits(self) -> int:
        return self._completed_credits


class UndergraduateStudent(Student):
    def get_responsibilities(self) -> str:
        return "Undergraduate: Attend lectures, complete assignments, participate in clubs, maintain full-time status"

    def is_full_time(self) -> bool:
        """Check if student is enrolled full-time (≥12 credits)."""
        return len(self._enrolled_courses) * self.CREDITS_PER_COURSE >= 12


class GraduateStudent(Student):
    MAX_COURSES = 4  # Graduate students have lower course limits
    
    def get_responsibilities(self) -> str:
        return "Graduate: Research, attend seminars, assist in teaching, publish papers"

    def can_graduate(self) -> bool:
        """Check if graduate student meets graduation requirements."""
        return (self._completed_credits >= 30 and 
                self._gpa >= 3.0 and 
                all(self._is_course_passed(code) for code in self._grades.keys()))


class SecureStudentRecord(Student):
    """Enhanced with better encryption simulation and audit logging."""
    
    def __init__(self, name: str, id_number: str, email: str):
        super().__init__(name, id_number, email)
        self.__ssn = None
        self.__encryption_key = "university_secure_key_2024"
        self._access_log = []

    def _encrypt(self, data: str) -> str:
        """Simulate encryption for sensitive data."""
        # In a real system, use proper encryption like AES
        return f"ENCRYPTED_{data}_{self.__encryption_key}"

    def _decrypt(self, encrypted_data: str) -> str:
        """Simulate decryption."""
        if encrypted_data.startswith("ENCRYPTED_"):
            return encrypted_data.replace(f"ENCRYPTED_", "").replace(f"_{self.__encryption_key}", "")
        return encrypted_data

    def set_ssn(self, ssn: str) -> None:
        """Set SSN with enhanced validation and encryption."""
        if not isinstance(ssn, str) or not re.match(r'^\d{9}$', ssn):
            raise ValueError("SSN must be 9 digits")
        
        self.__ssn = self._encrypt(ssn)
        self._log_access(f"SSN set for {self._name}")

    def get_ssn(self) -> str:
        """Get decrypted SSN with access logging."""
        self._log_access(f"SSN accessed for {self._name}")
        return self._decrypt(self.__ssn) if self.__ssn else None

    def set_gpa(self, gpa: float) -> None:
        """Override GPA setting with enhanced validation."""
        if not 0.0 <= gpa <= 4.0:
            raise ValueError("GPA must be between 0.0 and 4.0")
        self._gpa = gpa
        self._log_access(f"GPA manually set to {gpa} for {self._name}")
    
    def get_gpa(self):
        self._access_log.append("GPA accessed")
        return self._gpa

    def _log_access(self, action: str) -> None:
        """Log access to sensitive data."""
        import datetime
        log_entry = f"{datetime.datetime.now()}: {action}"
        self._access_log.append(log_entry)

    def get_access_log(self) -> List[str]:
        """Get access log for audit purposes."""
        return self._access_log.copy()