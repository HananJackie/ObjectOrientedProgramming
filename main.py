from class_ex.student import Student
from class_ex.course import Course

grisha = Student('Grisha', 1, 23, 'grisha@gmail.com', 1)
yonit = Student('Yonit', 2, 25, 'yonit@gmail.com', 1)
johnny = Student('Johnny', 3, 29, 'johnny@gmail.com', 2)

algebra = Course('Algebra', 2)
computer_science = Course('Computer Science', 2)

algebra.print_registered_students()

algebra.register_student(grisha)
algebra.register_student(yonit)
algebra.register_student(johnny)

computer_science.register_student(yonit)
computer_science.register_student(johnny)
computer_science.register_student(grisha)

algebra.print_registered_students()
computer_science.print_registered_students()

