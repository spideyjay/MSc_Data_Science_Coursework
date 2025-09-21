class Course:
    def __init__(self, code, name, capacity=30, prerequisites=None):
        self.code = code
        self.name = name
        self.capacity = capacity
        self.prerequisites = prerequisites if prerequisites else []
        self.students = []
        self.faculty = None

    def add_student(self, student):
        if len(self.students) >= self.capacity:
            print(f"Course {self.code} is full.")
            return False
        # Prerequisite check
        for prereq in self.prerequisites:
            if prereq not in [c.code for c in student._enrolled_courses]:
                print(f"Missing prerequisite: {prereq}")
                return False
        self.students.append(student)
        return True

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def assign_faculty(self, faculty):
        self.faculty = faculty
