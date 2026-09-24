class Teacher:

    def __init__(self, name, age, teaching_subjects):
        self.name = name
        self.age = age
        self.teaching_subjects = teaching_subjects

    def print_teacher_details(self):
        print(f"Teacher Name: {self.name}")
        print(f"Teacher age: {self.age}")
        print(f"Teacher Subjects: {self.teaching_subjects}")


class Course:

    def __init__(self, course_name, course_size, course_teacher):
        self.course_name = course_name
        self.course_size = course_size
        self.course_teacher = course_teacher

    def print_course_details(self):
        print(f"Course Name: {self.course_name}")
        print(f"Max amount of students: {self.course_size}")
        self.course_teacher.print_teacher_details()

if __name__ == '__main__':
    my_teacher = Teacher("Dana Almog", 42, ["AI Developer", "Backend Developer", "Fullstack Developer"])
    my_course = Course("AI Developer", 25, my_teacher)
    my_course.print_course_details()