# main.py
from person import Person, Staff
from student import Student, UndergraduateStudent, GraduateStudent, SecureStudentRecord
from faculty import Faculty, Professor, Lecturer, TA
from course import Course
from department import Department

# Create persons
alice = UndergraduateStudent("Alice", "U001")
bob = GraduateStudent("Bob", "G001")
prof = Professor("Dr. Smith", "F001", "CS")
lect = Lecturer("Ms. Lee", "F002", "Math")
ta = TA("Tom", "F003", "CS")
staff = Staff("Jane", "S001", "Admin")

# Create courses
cs101 = Course("CS101", "Intro to CS", capacity=2)
cs201 = Course("CS201", "Data Structures", prerequisites=["CS101"])
math101 = Course("MATH101", "Calculus")

# Create department
cs_dept = Department("Computer Science")
cs_dept.add_faculty(prof)
cs_dept.add_faculty(lect)
cs_dept.add_faculty(ta)
cs_dept.add_course(cs101)
cs_dept.add_course(cs201)
cs_dept.add_course(math101)
cs_dept.assign_faculty_to_course(prof, cs101)
cs_dept.assign_faculty_to_course(lect, math101)

# Assign students to department
cs_dept.assign_student_to_department(alice)
cs_dept.assign_student_to_department(bob)

# Enroll students
alice.enroll_course(cs101)
alice.enroll_course(cs201)  # Should fail due to missing prerequisite
bob.enroll_course(cs101)
bob.enroll_course(math101)

# Add grades and check GPA/status
alice.add_grade("CS101", 4)
alice.add_grade("CS101", 3)
print("Alice GPA:", alice.calculate_gpa())
print("Alice Status:", alice.get_academic_status())

# Polymorphism demonstration
people = [alice, bob, prof, lect, ta, staff]
for person in people:
    print(f"{person.get_name()} responsibilities: {person.get_responsibilities()}")

# SecureStudentRecord example
secure_student = SecureStudentRecord("Eve", "U999")
secure_student.set_ssn("123456789")
secure_student.set_gpa(3.5)
print("Secure student SSN:", secure_student.get_ssn())
print("Secure student GPA:", secure_student.get_gpa())