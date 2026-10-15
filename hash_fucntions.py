from class_ex.student import Student

HASH_TABLE_SIZE = 100000
hash_table = [[] for i in range(HASH_TABLE_SIZE)]

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __hash__(self):
        return hash((self.name, self.age, self.grade))

    def __eq__(self, other):
        return (self.name, self.age, self.grade, id(self)) == (other.name, other.age, other.grade, id(other))

    def __str__(self):
        return f'student(name={self.name}, age={self.age}, grade={self.grade})'

    def __repr__(self):
        return f'Student(name={self.name}, age={self.age}, grade={self.grade})'


def hash_function(key):
    return sum([ord(c) for c in key]) % HASH_TABLE_SIZE


def inset(student):
    hash_table[hash_function(student['name'])].append(student)

def get(student_name):
    for student in hash_table[hash_function(student_name)]:
        if student['name'] == student_name:
            return student

student_1 = Student(name='Cole', age=15, grade=10)
student_2 = Student(name='Cleo', age=16, grade=10)
student_3 = Student(name='Ada', age=15, grade=10)
student_4 = Student(name='Ada', age=15, grade=10)


students = {
    student_1: student_1,
    student_2: student_2,
    student_3: student_3,
    student_4: student_4
}
print(student_1 == student_4)
print(student_3 == student_4)

for student in students:
    print(student)