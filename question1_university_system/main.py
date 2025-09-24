# main.py
from person import Person, Staff
from student import Student, UndergraduateStudent, GraduateStudent, SecureStudentRecord
from faculty import Faculty, Professor, Lecturer, TA
from course import Course
from department import Department

def main():
    print("=== Enhanced University Management System ===\n")
    
    # Create persons with validation
    try:
        danesh = UndergraduateStudent("Danesh Jayasinghe", "U001", "danesh@university.edu")
        ashan = GraduateStudent("Ashan Jayaweera", "G001", "ashan@university.edu")
        prof = Professor("Dr Jayasinghe", "F001", "Jayasinghe@cs.edu", "Computer Science")
        lect = Lecturer("Ms Costa", "F002", "Costa@math.edu", "Mathematics")
        ta = TA("Goyum Perera", "F003", "Goyum@cs.edu", "Computer Science", prof)
        staff = Staff("Randula Silva", "S001", "Randula@admin.edu", "Admin")
        
        # Test invalid data (commented out to avoid errors)
        # invalid_student = UndergraduateStudent("123Invalid", "ID1", "invalid-email")
    except ValueError as e:
        print(f"Validation error: {e}")

    # Create courses with credits
    cs101 = Course("CS101", "Intro to Computer Science", credits=4, capacity=2)
    cs201 = Course("CS201", "Data Structures", credits=4, prerequisites=["CS101"])
    math101 = Course("MATH101", "Calculus I", credits=3)
    cs301 = Course("CS301", "Advanced Algorithms", credits=3, prerequisites=["CS201"])

    # Create department
    cs_dept = Department("Computer Science")
    cs_dept.add_faculty(prof)
    cs_dept.add_faculty(ta)
    cs_dept.add_course(cs101)
    cs_dept.add_course(cs201)
    cs_dept.add_course(cs301)
    cs_dept.assign_student_to_department(danesh)
    cs_dept.assign_student_to_department(ashan)

    # Assign faculty to courses
    cs_dept.assign_faculty_to_course(prof, cs101)
    cs_dept.assign_faculty_to_course(prof, cs301)

    print("=== Course Enrollment Demo ===")
    # Enroll students with enhanced system
    try:
        danesh.enroll_course(cs101)
        danesh.enroll_course(math101)  # Different department
        ashan.enroll_course(cs101)
        
        # Try to enroll in course with missing prerequisite
        danesh.enroll_course(cs201)  # Should fail - missing CS101 grade
    except ValueError as e:
        print(f"Enrollment error: {e}")

    # Add grades with credit-based GPA calculation
    print("\n=== Grading System Demo ===")
    danesh.add_grade("CS101", 3.8)  # A grade
    danesh.add_grade("MATH101", 3.2)  # B grade
    
    # Calculate credit-weighted GPA
    print(f"Danesh GPA: {danesh.calculate_gpa()} (Credit-weighted)")
    print(f"Danesh Status: {danesh.get_academic_status()}")
    print(f"Danesh Completed Credits: {danesh.completed_credits}")
    
    # Generate transcript
    transcript = danesh.get_transcript()
    print(f"\nDanesh Transcript: {transcript}")

    print("\n=== Waitlist System Demo ===")
    # Create more students to demonstrate waitlist
    sachini = UndergraduateStudent("Sachini Silva", "U002", "sachini@university.edu")
    dimanthi = UndergraduateStudent("Dimanthi Prince", "U003", "dimanthi@university.edu")
    
    cs_dept.assign_student_to_department(sachini)
    cs_dept.assign_student_to_department(dimanthi)
    
    # Try to enroll in full course
    sachini.enroll_course(cs101)  # Should go to waitlist
    dimanthi.enroll_course(cs101)   # Should also go to waitlist
    
    print(f"CS101 Waitlist: {[s.name for s in cs101.waitlist]}")
    print(f"Sachini waitlist position: {cs101.get_waitlist_position(sachini)}")

    # Demonstrate dropping and waitlist activation
    danesh.drop_course(cs101)
    print(f"After drop - CS101 enrolled: {[s.name for s in cs101.students]}")
    print(f"Remaining waitlist: {[s.name for s in cs101.waitlist]}")

    print("\n=== Polymorphism Demo ===")
    people = [danesh, ashan, prof, lect, ta, staff]
    for person in people:
        responsibilities = person.get_responsibilities()
        print(f"{person.name:15} | {person.__class__.__name__:12} | {responsibilities}")

    print("\n=== Workload Calculation Demo ===")
    workloads = [prof.calculate_workload(), ta.calculate_workload()]
    for workload in workloads:
        print(f"Workload: {workload}")

    print("\n=== Secure Student Record Demo ===")
    secure_student = SecureStudentRecord("Huda Dole", "U999", "huda@secure.edu")
    secure_student.set_ssn("123456789")
    secure_student.set_gpa(3.7)
    
    print(f"Secure student SSN: {secure_student.get_ssn()}")
    print(f"Secure student GPA: {secure_student.get_gpa()}")
    print(f"Access log: {secure_student.get_access_log()}")

    print("\n=== Department Statistics ===")
    stats = cs_dept.get_department_stats()
    print(f"Department: {stats['department']}")
    print(f"Faculty: {stats['faculty_count']}, Courses: {stats['course_count']}, Students: {stats['student_count']}")
    
    overenrolled = cs_dept.get_overenrolled_courses()
    if overenrolled:
        print(f"Overenrolled courses: {[course.code for course in overenrolled]}")

if __name__ == "__main__":
    main()