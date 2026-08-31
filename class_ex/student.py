class Student:
    name = 'Unknown'
    student_id = 0
    age = 18
    email = 'Unknown'
    academic_year = 1

    def __init__(self, name, student_id, age, email, academic_year):
        self.name = name
        self.student_id = student_id
        self.age = age
        self.email = email
        self.academic_year = academic_year


    def print(self):
        print(f'Student {self.name} {self.age} years old, id: {self.student_id}, email: {self.email}, AY: {self.academic_year}')

if __name__ == '__main__':
    student = Student('Jackie', 123456789, 35, 'jackie@gmail.com',2)
    student.print()