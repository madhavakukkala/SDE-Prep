class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # Instance Method
    def get_info(self):
        return f"{self.name} = {self.gpa}"
    
    # Class method
    @classmethod
    def get_count(cls):
        return f"Total number of students {cls.count}"
    @classmethod
    def get_average(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Total average {cls.total_gpa/cls.count:.2f}"

student1 = Student("karthik", 3.2)
student2 = Student("Kavya", 2.0)
student3 = Student("Keerthi", 4.0)

print(student1.get_info())
print(student2.get_info())
print(student3.get_info())

print(Student.get_count())
print(Student.get_average())