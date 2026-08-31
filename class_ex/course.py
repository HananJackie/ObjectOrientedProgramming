class Course:
    def __init__(self, course_name, max_size):
        self.course_name = course_name
        self.max_size = max_size
        self.students = []

    def register_student(self, student):
        if len(self.students) < self.max_size:
            self.students.append(student)
            print('Registration succeeded')
        else:
            print('Registration failed!')

    def print_registered_students(self):
        print(f'Registered students in course {self.course_name}:')
        for student in self.students:
            student.print()

