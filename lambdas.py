def func(param1, param2):
    return param1 + param2

print(func(4,7))

print((lambda param1, param2: param1 + param2)(4, 7))


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __repr__(self):
        return f'{self.name}: {self.grade}'

    def __lt__(self, other):
        return self.grade < other.grade

students = [
    Student('A', 85),
    Student('B', 59),
    Student('C', 98),
    Student('D', 76),
    Student('E', 87),
    Student('F', 23),
    Student('G', 87),
]

students.sort(reverse=True)
print(students)