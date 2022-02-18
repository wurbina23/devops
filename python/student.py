class Student:
    def __init__(self, name, age, grade):
        self.name = name 
        self.age = age
        self.grade = grade # 0 - 100

    def get_grade(self):
        return self.grade

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


# another class 
class Course:
    def __init__(self, name, max_students):
        self.name = name 
        self.max_students = max_students
        # empty attribute and it is fine 
        self.students = []
        # self.is_active = False

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True 
        else:
            return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)


s1 = Student("Walter", 19, 90)
s2 = Student("Bladi", 19, 75)  
s3 = Student("Mary", 19, 85)  

# Setup new course
course = Course("Math", 2)
course.add_student(s1)
course.add_student(s2)
print(course.add_student(s3))

print(f"{course.students[0].grade}")

print(f"{course.get_average_grade()}")
