class Student:
    school_name = "ABC high School"
    a = self

    def __init__(self , name, course):
        self.name= name
        self.course= course

    def start(self):
        print("This is the start method ")


student1 = Student("khushi", "B.tech") # __init__ method will be called by defualt automatically
print(f"Student1 Name: {student1.name}")
print(f"Student1 Course: {student1.course}")

student2 = Student("Nandhini", "MS")
print(f"Student2 Name: {student2.name}")
print(f"Student2 Course: {student2.course}")

student1.start()

