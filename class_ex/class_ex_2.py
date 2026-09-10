from collections import Counter
from enum import Enum


class Course(Enum):
    AI = 1
    FULLSTACK = 2
    QA = 3
    CYBER = 4
    PRODUCT_MANAGEMENT = 5


class Student:
    def __init__(self, student_id, name, age, email, course: Course):
        if not isinstance(course, Course):
            raise TypeError("course must be an instance of Course Enum")
        self.student_id = student_id
        self.name = name
        self.age = age
        self.email = email
        self.course = course

def print_course_counts(students):
    # counts = {}
    # for student in students:
    #     if student.course not in counts:
    #         counts[student.course] = 0
    #     counts[student.course] += 1
    counts = Counter(student.course for student in students)
    for course in Course:
        print(f'{course.name} has {counts[course]} students')

courses = list(Course)
students = [
    Student(
        i,
        f'student_{i}',
        20 + i % 7,
        f'student_{i}@gmail.com',
        courses[i % len(courses)])
    for i in range(1,30)]

print_course_counts(students)