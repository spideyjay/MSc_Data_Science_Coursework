# main.py
from person import Person
from student import Student, UndergraduateStudent, GraduateStudent
from faculty import Faculty, Professor, Lecturer, TA
from department import Department
from course import Course

if __name__ == "__main__":
    # Create instances of departments and courses
    ds_dept = Department("Data Science")
    ai_course = Course("Introduction to AI", "DSAI101", 3, 50)
    prog_course = Course("Programming for DS", "DSPR202", 4, 40)
    ds_dept.add_course(ai_course)
    ds_dept.add_course(prog_course)

    # Create instances of different person types
    student1 = UndergraduateStudent("Alice Johnson", "S1001", "alice.j@uni.edu")
    student2 = GraduateStudent("Bob Smith", "S2001", "bob.s@uni.edu")
    professor1 = Professor("Dr. Emily White", "F3001", "e.white@uni.edu")

    # Demonstrate polymorphism
    person_list = [student1, professor1]
    for person in person_list:
        print(f"{person.name}'s responsibilities: {person.get_responsibilities()}")

    # Demonstrate course enrollment with validation
    try:
        student1.gpa = 3.7
        print(f"{student1.name}'s GPA set to {student1.gpa}")
        print(f"{student1.name}'s academic status: {student1.get_academic_status()}")

        # This will raise a ValueError
        student1.gpa = 5.0
    except ValueError as e:
        print(f"Error: {e}")

    student1.enroll_course(ai_course)
    student1.enroll_course(prog_course)