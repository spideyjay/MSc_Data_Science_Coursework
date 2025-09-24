# university_system/course.py
from typing import List, Optional
from typing import Dict

class Course:
    """
    A class to represent a university course with waitlist functionality.
    """
    
    def __init__(self, code: str, name: str, credits: int = 3, capacity: int = 30, 
                 prerequisites: Optional[List[str]] = None):
        self.code = code
        self.name = name
        self.credits = credits
        self.capacity = capacity
        self.prerequisites = prerequisites if prerequisites else []
        self.students = []  # Enrolled students
        self.waitlist = []  # Students waiting for enrollment
        self.faculty = None
        self.schedule = None  # Could be expanded with time/day/location

    def add_student(self, student) -> bool:
        """Enroll student or add to waitlist if course is full."""
        if len(self.students) >= self.capacity:
            if student not in self.waitlist:
                self.waitlist.append(student)
            return False  # Added to waitlist
        
        # Check prerequisites (student handles this now, but double-check)
        self.students.append(student)
        
        # If student was on waitlist, remove them
        if student in self.waitlist:
            self.waitlist.remove(student)
            
        return True

    def remove_student(self, student) -> bool:
        """Remove student and enroll first waitlisted student if any."""
        if student in self.students:
            self.students.remove(student)
            
            # Enroll first student from waitlist if available
            if self.waitlist:
                next_student = self.waitlist.pop(0)
                self.students.append(next_student)
                print(f"Enrolled {next_student.name} from waitlist to {self.code}")
            
            return True
        return False

    def assign_faculty(self, faculty) -> None:
        """Assign faculty member to teach the course."""
        self.faculty = faculty

    def get_enrollment_info(self) -> Dict:
        """Get detailed enrollment information."""
        return {
            'course': f"{self.code} - {self.name}",
            'enrolled': len(self.students),
            'capacity': self.capacity,
            'waitlist_count': len(self.waitlist),
            'available_seats': self.capacity - len(self.students),
            'credits': self.credits
        }

    def is_full(self) -> bool:
        return len(self.students) >= self.capacity

    def get_waitlist_position(self, student) -> int:
        """Get student's position in waitlist (0-based, -1 if not found)."""
        try:
            return self.waitlist.index(student)
        except ValueError:
            return -1

    def __str__(self) -> str:
        return f"{self.code}: {self.name} ({self.credits} credits)"

    def __repr__(self) -> str:
        return f"Course('{self.code}', '{self.name}', {self.credits}, {self.capacity})"